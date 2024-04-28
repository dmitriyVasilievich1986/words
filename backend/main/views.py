from .models import Declentions, Gender, Time, Preposition, Tags, Infinitive, PartsOfSpeech
from rest_framework.exceptions import MethodNotAllowed, ValidationError
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from verb.serializer import VerbSerializer
from pronoun.models import PersonalPronoun
from django.shortcuts import render
from rest_framework import status
from verb.models import Verb

from .serializer import (
    InfinitiveSerializerDeep,
    InfinitiveTagsSerializer,
    PartsOfSpeechSerializer,
    PrepositionSerializer,
    DeclentionsSerializer,
    InfinitiveSerializer,
    GenderSerializer,
    TimeSerializer,
    TagsSerializer,
)


def index_view(request, *args, **kwargs):
    return render(request, "index.html")


class PrepositionViewSet(ModelViewSet):
    serializer_class = PrepositionSerializer
    queryset = Preposition.objects.all()


class TagsViewSet(ModelViewSet):
    serializer_class = TagsSerializer
    queryset = Tags.objects.all()


class DeclentionsViewSet(ModelViewSet):
    serializer_class = DeclentionsSerializer
    queryset = Declentions.objects.all()


class GenderViewSet(ModelViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()


class TimeViewSet(ModelViewSet):
    serializer_class = TimeSerializer
    queryset = Time.objects.all()

class InfinitiveViewSet(ModelViewSet):
    serializer_class = InfinitiveSerializerDeep
    queryset = Infinitive.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = InfinitiveSerializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE")

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        for verb in request.data.get("verb", []):
            if verb.get("id"):
                verb_instance = Verb.objects.get(id=verb.get("id"))
                verb_serializer = VerbSerializer(instance=verb_instance, data=verb)
            else:
                verb_serializer = VerbSerializer(data=verb)
            verb_serializer.is_valid(raise_exception=True)
            verb_serializer.save()
        if request.data.get("tags", None) is not None:
            self._update_tags(serializer.instance, request.data["tags"])

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        verbs = request.data.get("verb", [])
        if len(verbs) < PersonalPronoun.objects.count():
            raise ValidationError("You must provide a verb for each personal pronoun")
        self.perform_create(serializer)
        
        for verb in verbs:
            verb_serializer = VerbSerializer(data=verb | {"infinitive": serializer.instance.id})
            verb_serializer.is_valid(raise_exception=True)
            verb_serializer.save()
        if request.data.get("tags", None) is not None:
            self._update_tags(serializer.instance, request.data["tags"])

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def _update_tags(self, instance, tags):
        instance.tags.exclude(tags__in=tags).delete()
        for tag in tags:
            serializer = InfinitiveTagsSerializer(data={"infinitive": instance.id, "tags": tag})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            instance.tags.add(serializer.instance)

class PartsOfSpeechViewSet(ReadOnlyModelViewSet):
    serializer_class = PartsOfSpeechSerializer
    queryset = PartsOfSpeech.objects.all()

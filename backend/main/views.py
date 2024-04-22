from .models import Declentions, Gender, Time, Preposition, Tags, Infinitive, PartsOfSpeech, InfinitiveTags
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status

from .serializer import (
    InfinitiveSerializerDeep,
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

    def create(self, request, *args, **kwargs):
        serializer = InfinitiveSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if (tags := request.data.get("tags")) is not None:
            tags = Tags.objects.filter(id__in=tags)
            infinitive_tags = [
                InfinitiveTags.objects.create(tags=t, infinitive=serializer.instance)
                for t in tags
            ]
            serializer.instance.tags.set(infinitive_tags)
        serializer = InfinitiveSerializerDeep(serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if (tags := request.data.get("tags")) is not None:
            tags = Tags.objects.filter(id__in=tags)
            InfinitiveTags.objects.filter(infinitive=instance).exclude(tags__in=tags).delete()
            infinitive_tags = [
                InfinitiveTags.objects.get_or_create(tags=t, infinitive=instance)[0]
                for t in tags
            ]
            instance.tags.set(infinitive_tags)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class PartsOfSpeechViewSet(ReadOnlyModelViewSet):
    serializer_class = PartsOfSpeechSerializer
    queryset = PartsOfSpeech.objects.all()

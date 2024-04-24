from .models import Declentions, Gender, Time, Preposition, Tags, Infinitive, PartsOfSpeech
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response
from django.shortcuts import render

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

    def destroy(self, request, *args, **kwargs):
        raise MethodNotAllowed("DELETE")

class PartsOfSpeechViewSet(ReadOnlyModelViewSet):
    serializer_class = PartsOfSpeechSerializer
    queryset = PartsOfSpeech.objects.all()

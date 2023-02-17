from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from random import choice
import json

from .models import (
    PersonalPronoun,
    VerbInfinitive,
    NounInfinitive,
    Declentions,
    Pronoun,
    Gender,
    Verb,
    Noun,
)

from .serializer import (
    PersonalPronounSerializer,
    VerbInfinitiveSerializer,
    NounInfinitiveSerializer,
    DeclentionsSerializer,
    PronounSerializer,
    GenderSerializer,
    NounSerializer,
    VerbSerializer,
)


class VerbInfinitiveViewSet(ModelViewSet):
    serializer_class = VerbInfinitiveSerializer
    queryset = VerbInfinitive.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        payload = serializer.data
        if request.GET:
            instance = choice(
                instance.verb.filter(
                    **{k: request.GET[k] for k, v in dict(request.GET).items()}
                )
            )
            serializer = VerbSerializer(instance=instance)
            payload["verb"] = serializer.data
        return Response(payload)


class PronounViewSet(ModelViewSet):
    serializer_class = PronounSerializer
    queryset = Pronoun.objects.all()


class NounInfinitiveViewSet(ModelViewSet):
    serializer_class = NounInfinitiveSerializer
    queryset = NounInfinitive.objects.all()


class NounViewSet(ModelViewSet):
    serializer_class = NounSerializer
    queryset = Noun.objects.all()


class PersonalPronounViewSet(ModelViewSet):
    serializer_class = PersonalPronounSerializer
    queryset = PersonalPronoun.objects.all()


class VerbViewSet(ModelViewSet):
    serializer_class = VerbSerializer
    queryset = Verb.objects.all()


class DeclentionsViewSet(ModelViewSet):
    serializer_class = DeclentionsSerializer
    queryset = Declentions.objects.all()


class GenderViewSet(ModelViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()

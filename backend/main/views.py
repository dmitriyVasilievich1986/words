from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, exceptions
from rest_framework.response import Response

from .models import (
    PersonalPronoun,
    VerbInfinitive,
    NounInfinitive,
    RANDOM_CHOICES,
    Declentions,
    Pronoun,
    Gender,
    Verb,
    Noun,
    Time,
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
    TimeSerializer,
)


class SimpleListViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet,
):
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        payload = [
            {k: v for k, v in x.items() if not isinstance(v, list)}
            for x in serializer.data
        ]
        return Response(payload)


class RandomChoicesViewSet(GenericViewSet):
    def retrieve(self, request, pk, *args, **kwargs):
        if int(pk) >= len(RANDOM_CHOICES):
            raise exceptions.NotFound
        return Response(
            RANDOM_CHOICES[int(pk)].random(
                **{k: request.GET[k] for k, v in dict(request.GET).items()}
            )
        )

    def list(self, request, *args, **kwargs):
        return Response([x.json() for x in RANDOM_CHOICES])


class VerbInfinitiveViewSet(SimpleListViewSet):
    serializer_class = VerbInfinitiveSerializer
    queryset = VerbInfinitive.objects.all()


class PronounViewSet(SimpleListViewSet):
    serializer_class = PronounSerializer
    queryset = Pronoun.objects.all()


class NounInfinitiveViewSet(SimpleListViewSet):
    serializer_class = NounInfinitiveSerializer
    queryset = NounInfinitive.objects.all()


class NounViewSet(SimpleListViewSet):
    serializer_class = NounSerializer
    queryset = Noun.objects.all()


class PersonalPronounViewSet(SimpleListViewSet):
    serializer_class = PersonalPronounSerializer
    queryset = PersonalPronoun.objects.all()


class VerbViewSet(SimpleListViewSet):
    serializer_class = VerbSerializer
    queryset = Verb.objects.all()


class DeclentionsViewSet(SimpleListViewSet):
    serializer_class = DeclentionsSerializer
    queryset = Declentions.objects.all()


class GenderViewSet(SimpleListViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()


class TimeViewSet(SimpleListViewSet):
    serializer_class = TimeSerializer
    queryset = Time.objects.all()

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import mixins

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

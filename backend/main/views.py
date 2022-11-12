from rest_framework.viewsets import ModelViewSet
from .models import Pron, Verb, VerbDeclension, Noun, Case, NounCase

from .serializer import (
    VerbDeclensionSerializer,
    PronSerializer,
    VerbSerializer,
    NounCaseSerializer,
    NounSerializer,
    CaseSerializer,
)


class NounCaseViewSet(ModelViewSet):
    serializer_class = NounCaseSerializer
    queryset = NounCase.objects.all()


class CaseViewSet(ModelViewSet):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()


class NounViewSet(ModelViewSet):
    serializer_class = NounSerializer
    queryset = Noun.objects.all()


class PronViewSet(ModelViewSet):
    serializer_class = PronSerializer
    queryset = Pron.objects.all()


class VerbViewSet(ModelViewSet):
    serializer_class = VerbSerializer
    queryset = Verb.objects.all()


class VerbDeclensionViewSet(ModelViewSet):
    serializer_class = VerbDeclensionSerializer
    queryset = VerbDeclension.objects.all()

from .serializer import PronSerializer, VerbSerializer, VerbDeclensionSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Pron, Verb, VerbDeclension


class PronViewSet(ModelViewSet):
    serializer_class = PronSerializer
    queryset = Pron.objects.all()


class VerbViewSet(ModelViewSet):
    serializer_class = VerbSerializer
    queryset = Verb.objects.all()


class VerbDeclensionViewSet(ModelViewSet):
    serializer_class = VerbDeclensionSerializer
    queryset = VerbDeclension.objects.all()

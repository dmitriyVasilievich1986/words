from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from .models import WordModel

MODELS = [WordModel(word="Глагол", url="/api/verb/")]


class ModelViewSet(GenericViewSet):
    def list(self, request, *args, **kwargs):
        return Response([{"id": i, **x} for i, x in enumerate(MODELS)])

from rest_framework.viewsets import ModelViewSet
from .serializer import VerbSerializer
from .models import Verb


class VerbViewSet(ModelViewSet):
    serializer_class = VerbSerializer
    queryset = Verb.objects.all()

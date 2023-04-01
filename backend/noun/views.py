from rest_framework.viewsets import ModelViewSet
from .serializer import NounSerializer
from .models import Noun


class NounViewSet(ModelViewSet):
    serializer_class = NounSerializer
    queryset = Noun.objects.all()

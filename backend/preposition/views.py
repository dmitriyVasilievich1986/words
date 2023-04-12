from rest_framework.viewsets import ModelViewSet
from .serializer import PrepositionSerializer
from .models import Preposition


class PrepositionViewSet(ModelViewSet):
    serializer_class = PrepositionSerializer
    queryset = Preposition.objects.all()

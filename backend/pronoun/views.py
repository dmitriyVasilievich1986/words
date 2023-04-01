from rest_framework.viewsets import ModelViewSet
from .serializer import PronounSerializer
from .models import Pronoun


class PronounViewSet(ModelViewSet):
    serializer_class = PronounSerializer
    queryset = Pronoun.objects.all()

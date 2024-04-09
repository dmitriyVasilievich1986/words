from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializer import PronounSerializer, PersonalPronounSerializer
from .models import Pronoun, PersonalPronoun


class PronounViewSet(ModelViewSet):
    serializer_class = PronounSerializer
    queryset = Pronoun.objects.all()

class PersonalPronounViewSet(ReadOnlyModelViewSet):
    serializer_class = PersonalPronounSerializer
    queryset = PersonalPronoun.objects.all()

from .models import Declentions, Gender, Time, Preposition
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render

from .serializer import (
    PrepositionSerializer,
    DeclentionsSerializer,
    GenderSerializer,
    TimeSerializer,
)


def index_view(request, *args, **kwargs):
    return render(request, "index.html")


class PrepositionViewSet(ModelViewSet):
    serializer_class = PrepositionSerializer
    queryset = Preposition.objects.all()


class DeclentionsViewSet(ModelViewSet):
    serializer_class = DeclentionsSerializer
    queryset = Declentions.objects.all()


class GenderViewSet(ModelViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()


class TimeViewSet(ModelViewSet):
    serializer_class = TimeSerializer
    queryset = Time.objects.all()

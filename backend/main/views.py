from .serializer import DeclentionsSerializer, GenderSerializer, TimeSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Declentions, Gender, Time
from django.shortcuts import render


def index_view(request, pk=None):
    return render(request, "index.html")


class DeclentionsViewSet(ModelViewSet):
    serializer_class = DeclentionsSerializer
    queryset = Declentions.objects.all()


class GenderViewSet(ModelViewSet):
    serializer_class = GenderSerializer
    queryset = Gender.objects.all()


class TimeViewSet(ModelViewSet):
    serializer_class = TimeSerializer
    queryset = Time.objects.all()

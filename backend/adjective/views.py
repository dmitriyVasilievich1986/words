from models.models import TextInput, ChoiceInput, BoolInput
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import AdjectiveSerializer
from main.models import Gender
from .models import Adjective


class AdjectiveViewSet(ModelViewSet):
    serializer_class = AdjectiveSerializer
    queryset = Adjective.objects.all()

    @action(detail=False, methods=["get"])
    def model(self, *args, **kwargs):
        g = [{"id": x.id, "word": x.word} for x in Gender.objects.all()]
        payload = [
            TextInput(name="base", text="base"),
            TextInput(name="word", text="word"),
            TextInput(name="translate", text="translate"),
            BoolInput(name="plural", text="plural"),
            ChoiceInput(name="gender", text="gender", value=g),
        ]
        return Response(payload)

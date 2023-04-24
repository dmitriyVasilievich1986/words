from models.models import TextInput, ChoiceInput, BoolInput
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from main.models import Gender, Preposition
from .serializer import NounSerializer
from .models import Noun


class NounViewSet(ModelViewSet):
    serializer_class = NounSerializer
    queryset = Noun.objects.all()

    @action(detail=False, methods=["get"])
    def model(self, *args, **kwargs):
        p = [{"id": x.id, "word": x.word} for x in Preposition.objects.all()]
        g = [{"id": x.id, "word": x.word} for x in Gender.objects.all()]
        payload = [
            TextInput(name="base", text="base"),
            TextInput(name="word", text="word"),
            TextInput(name="translate", text="translate"),
            BoolInput(name="plural", text="plural"),
            ChoiceInput(name="gender", text="gender", value=g),
            ChoiceInput(
                name="prepositions", text="prepositions", value=p, multiple=True
            ),
        ]
        return Response(payload)

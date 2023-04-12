from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from models.models import TextInput, ChoiceInput
from rest_framework.response import Response
from main.models import Time, Declentions
from .serializer import VerbSerializer
from pronoun.models import Pronoun
from .models import Verb


class VerbViewSet(ModelViewSet):
    serializer_class = VerbSerializer
    queryset = Verb.objects.all()

    @action(detail=False, methods=["get"])
    def model(self, *args, **kwargs):
        d = Declentions.objects.get(word="Nominative").id
        p = [{"id": x.id, "word": x.word} for x in Pronoun.objects.filter(declention=d)]
        t = [{"id": x.id, "word": x.word} for x in Time.objects.all()]
        payload = [
            TextInput(name="word", text="word"),
            TextInput(name="base", text="base"),
            TextInput(name="translate", text="translate"),
            ChoiceInput(name="time", text="time", value=t),
            ChoiceInput(name="pronoun", text="pronoun", value=p),
        ]
        return Response(payload)

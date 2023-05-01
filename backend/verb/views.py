from main.models import Time, Declentions, Preposition, Tags
from rest_framework.viewsets import ModelViewSet
from models.models import TextInput, ChoiceInput
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import VerbSerializer
from main.support_mixin import RDict
from pronoun.models import Pronoun
from .models import Verb


class VerbViewSet(ModelViewSet):
    serializer_class = VerbSerializer
    queryset = Verb.objects.all()

    @action(detail=False, methods=["get"])
    def model(self, *args, **kwargs):
        time = [RDict(x) for x in Time.objects.all()]
        tags = [RDict(x) for x in Tags.objects.all()]
        d = Declentions.objects.get(word="Nominative")
        preposition = [RDict(x) for x in Preposition.objects.all()]
        pronoun = [RDict(x) for x in Pronoun.objects.filter(declention=d)]

        payload = [
            TextInput(name="word", text="word"),
            TextInput(name="base", text="base"),
            TextInput(name="translate", text="translate"),
            ChoiceInput(name="time", text="time", value=time),
            ChoiceInput(name="pronoun", text="pronoun", value=pronoun),
            ChoiceInput(name="tags", text="tags", value=tags, multiple=True),
            ChoiceInput(
                name="prepositions",
                text="prepositions",
                value=preposition,
                multiple=True,
            ),
        ]
        return Response(payload)

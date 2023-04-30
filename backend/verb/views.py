from main.models import Time, Declentions, Preposition, Tags
from rest_framework.viewsets import ModelViewSet
from models.models import TextInput, ChoiceInput
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import VerbSerializer
from pronoun.models import Pronoun
from .models import Verb


class VerbViewSet(ModelViewSet):
    serializer_class = VerbSerializer
    queryset = Verb.objects.all()

    @action(detail=False, methods=["get"])
    def model(self, *args, **kwargs):
        p = [{"id": x.id, "word": x.word} for x in Pronoun.objects.filter(declention=d)]
        preposition = [{"id": x.id, "word": x.word} for x in Preposition.objects.all()]
        tags = [{"id": x.id, "word": x.word} for x in Tags.objects.all()]
        t = [{"id": x.id, "word": x.word} for x in Time.objects.all()]
        d = Declentions.objects.get(word="Nominative").id

        payload = [
            TextInput(name="word", text="word"),
            TextInput(name="base", text="base"),
            TextInput(name="translate", text="translate"),
            ChoiceInput(name="time", text="time", value=t),
            ChoiceInput(name="pronoun", text="pronoun", value=p),
            ChoiceInput(name="tags", text="tags", value=tags, multiple=True),
            ChoiceInput(
                name="prepositions",
                text="prepositions",
                value=preposition,
                multiple=True,
            ),
        ]
        return Response(payload)

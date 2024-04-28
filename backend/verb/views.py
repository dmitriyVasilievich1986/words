from main.models import Infinitive, PartsOfSpeech, Time
from rest_framework.exceptions import ValidationError
from main.serializer import InfinitiveSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from pronoun.models import PersonalPronoun
from .serializer import VerbSerializer
from .models import Verb


class VerbViewSet(ModelViewSet):
    serializer_class = VerbSerializer
    queryset = Verb.objects.all()

    @action(detail=False, methods=["POST"])
    def infinitive(self, request):
        if "infinitive" not in request.data:
            raise ValidationError("Infinitive is required")
        queryset = Verb.objects.filter(infinitive=request.data["infinitive"])

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["GET"])
    def empty(self, request):
        payload = InfinitiveSerializer(Infinitive(word="", translate="", part_of_speech=PartsOfSpeech.objects.get(word="verb"))).data
        verb = VerbSerializer([
            Verb(word="", translate="", personal_pronoun=x, time=t)
            for x in PersonalPronoun.objects.all()
            for t in Time.objects.all()
        ], many=True).data
        return Response(
            payload | {"verb": verb, "tags": []}
        )

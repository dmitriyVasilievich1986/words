from main.models import Time, Declentions, Preposition, Tags
from rest_framework.viewsets import ModelViewSet
from models.models import TextInput, ChoiceInput
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import VerbSerializer
from main.support_mixin import RDict
from pronoun.models import Pronoun
from .models import Verb
from rest_framework.exceptions import ValidationError


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

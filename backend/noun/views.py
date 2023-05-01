from models.models import TextInput, ChoiceInput, BoolInput
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import NounSerializer
from main.support_mixin import RDict
from main.models import Gender, Tags
from .models import Noun


class NounViewSet(ModelViewSet):
    serializer_class = NounSerializer
    queryset = Noun.objects.all()

    @action(detail=False, methods=["get"])
    def model(self, *args, **kwargs):
        tags = [RDict(x) for x in Tags.objects.all()]
        g = [RDict(x) for x in Gender.objects.all()]

        payload = [
            TextInput(name="base", text="base"),
            TextInput(name="word", text="word"),
            TextInput(name="translate", text="translate"),
            BoolInput(name="plural", text="plural"),
            ChoiceInput(name="gender", text="gender", value=g),
            ChoiceInput(name="tags", text="tags", value=tags, multiple=True),
        ]
        return Response(payload)

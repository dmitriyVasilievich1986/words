from .models import Pron, Verb, VerbDeclension
from rest_framework.serializers import ModelSerializer


class PronSerializer(ModelSerializer):
    class Meta:
        model = Pron
        fields = "__all__"


class VerbSerializer(ModelSerializer):
    class Meta:
        model = Verb
        fields = "__all__"


class VerbDeclensionSerializer(ModelSerializer):
    class Meta:
        model = VerbDeclension
        fields = "__all__"

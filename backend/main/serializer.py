from .models import Pron, Verb, VerbDeclension, Noun, Case, NounCase
from rest_framework.serializers import ModelSerializer


class NounCaseSerializer(ModelSerializer):
    class Meta:
        model = NounCase
        fields = "__all__"


class CaseSerializer(ModelSerializer):
    class Meta:
        model = Case
        fields = "__all__"


class NounSerializer(ModelSerializer):
    class Meta:
        model = Noun
        fields = "__all__"


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

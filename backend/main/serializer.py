from .models import Pron, Verb, VerbDeclension, Noun, Case, NounCase, Adjective, AdjCase
from rest_framework.serializers import ModelSerializer


class AdjCaseSerializer(ModelSerializer):
    class Meta:
        model = AdjCase
        fields = "__all__"
        # fields = ["id", "word", "translate", "case", "adjective", "gender"]


class AdjectiveSerializer(ModelSerializer):
    class Meta:
        model = Adjective
        fields = "__all__"


class NounCaseSerializer(ModelSerializer):
    class Meta:
        model = NounCase
        fields = ["id", "word", "translate", "case", "noun", "gender"]

        read_only_fields = ["gender"]


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

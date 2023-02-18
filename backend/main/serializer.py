from rest_framework.serializers import ModelSerializer
from .models import (
    PersonalPronoun,
    VerbInfinitive,
    NounInfinitive,
    Declentions,
    Pronoun,
    Gender,
    Verb,
    Noun,
)


class VerbSerializer(ModelSerializer):
    class Meta:
        model = Verb
        fields = "__all__"


class VerbInfinitiveSerializer(ModelSerializer):
    verb = VerbSerializer(many=True, read_only=True)

    class Meta:
        model = VerbInfinitive
        fields = "__all__"


class NounSerializer(ModelSerializer):
    class Meta:
        model = Noun
        fields = "__all__"


class NounInfinitiveSerializer(ModelSerializer):
    noun = NounSerializer(many=True, read_only=True)

    class Meta:
        model = NounInfinitive
        fields = "__all__"


class PronounSerializer(ModelSerializer):
    class Meta:
        model = Pronoun
        fields = "__all__"


class DeclentionsSerializer(ModelSerializer):
    class Meta:
        model = Declentions
        fields = "__all__"


class GenderSerializer(ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"


class PersonalPronounSerializer(ModelSerializer):
    class Meta:
        model = PersonalPronoun
        fields = "__all__"

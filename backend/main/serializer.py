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
    Time,
)


class VerbSerializer(ModelSerializer):
    class Meta:
        model = Verb
        fields = "__all__"


class VerbInfinitiveSerializer(ModelSerializer):
    verb = VerbSerializer(many=True)

    class Meta:
        model = VerbInfinitive
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        verbs = validated_data.pop("verb")
        verb_infinitive = VerbInfinitive.objects.create(**validated_data)
        for verb in verbs:
            Verb.objects.create(infinitive=verb_infinitive, **verb)
        return verb_infinitive


class NounSerializer(ModelSerializer):
    class Meta:
        model = Noun
        fields = "__all__"


class NounInfinitiveSerializer(ModelSerializer):
    noun = NounSerializer(many=True, read_only=True)

    class Meta:
        model = NounInfinitive
        fields = "__all__"

    def create(self, validated_data):
        nouns = validated_data.pop("nouns")
        noun_infinitive = NounInfinitive.objects.create(**validated_data)
        for noun in nouns:
            Noun.objects.create(noun=noun_infinitive, **noun)
        return noun_infinitive


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


class TimeSerializer(ModelSerializer):
    class Meta:
        model = Time
        fields = "__all__"

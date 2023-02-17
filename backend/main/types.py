from graphene_django import DjangoObjectType

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


class PersonalPronounType(DjangoObjectType):
    class Meta:
        model = PersonalPronoun
        fields = ("id", "word", "translate", "plural", "verb")


class GenderType(DjangoObjectType):
    class Meta:
        model = Gender
        fields = ("id", "word", "translate", "pronoun", "noun")


class DeclentionsType(DjangoObjectType):
    class Meta:
        model = Declentions
        fields = ("id", "word", "translate", "verb")


class VerbInfinitiveType(DjangoObjectType):
    class Meta:
        model = VerbInfinitive
        fields = ("id", "word", "translate", "verb")


class VerbType(DjangoObjectType):
    class Meta:
        model = Verb
        fields = ("id", "word", "translate", "plural", "pron")


class NounInfinitiveType(DjangoObjectType):
    class Meta:
        model = NounInfinitive
        fields = ("id", "word", "translate", "noun")


class NounType(DjangoObjectType):
    class Meta:
        model = Noun
        fields = ("id", "word", "translate", "plural", "declention", "gender")


class PronounType(DjangoObjectType):
    class Meta:
        model = Pronoun
        fields = ("id", "word", "translate", "plural", "gender")

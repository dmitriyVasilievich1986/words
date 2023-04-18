from main.models import Time, Declentions, Gender
from adjective.models import Adjective
from random import randint, choice
from pronoun.models import Pronoun
from verb.models import Verb
from noun.models import Noun

from .support_classes import (
    _get_rand_from_three,
    WordWithoutTranslate,
    WordBaseAnswerList,
    AnswerList,
    Answer,
    Random,
    Empty,
    Word,
    Base,
)


def _get_verb_declentions():
    declention = Declentions.objects.get(word="Nominative").id
    time = Time.objects.get(word="Present").id
    pronoun = Pronoun.random(declention=declention)
    verb = Verb.random(time=time, pronoun=pronoun)
    return WordBaseAnswerList(main=pronoun, secondary=verb)


def _get_past_future_verb(word):
    declention = Declentions.objects.get(word="Nominative").id
    time = Time.objects.get(word=word).id
    pronoun = Pronoun.random(declention=declention)
    past_verb = Verb.objects.get(time=time, base="", pronoun=pronoun.id)
    verb = Verb.random(time=time, pronoun=None)
    return AnswerList(
        WordWithoutTranslate(instance=pronoun),
        WordBaseAnswerList(main=past_verb, secondary=verb),
    )


def _get_noun():
    declention = Declentions.objects.get(word="Nominative").id
    noun = Noun.random(declention=declention, plural=False)
    return AnswerList(Word(instance=noun, hiden=True))


def _get_noun_plural():
    declention = Declentions.objects.get(word="Nominative").id
    noun = Noun.random(declention=declention, plural=True)
    if randint(0, 1):
        return AnswerList(Base(instance=noun))
    return AnswerList(Word(instance=noun, hiden=True))


def _get_noun_dative():
    declention = Declentions.objects.get(word="Dative").id
    gender = Gender.random().id
    plural = bool(randint(0, 1))
    adjective = Adjective.random(declention=declention, gender=gender, plural=plural)
    noun = Noun.random(declention=declention, gender=gender, plural=plural)
    preposition = (
        Word(choice(noun.prepositions.all())) if noun.prepositions.count() else None
    )
    return AnswerList(
        preposition,
        Base(instance=adjective)
        if randint(0, 1)
        else Word(instance=adjective, hiden=True),
        Base(instance=noun) if randint(0, 1) else Word(instance=noun, hiden=True),
    )


def _get_verb():
    verb = Verb.random(pronoun=None, time=None)
    return AnswerList(Word(instance=verb, hiden=True))


RANDOM_CHOICES = [
    Random(
        func=_get_verb,
        name="Глагол",
        description="Переведите глагол:",
    ),
    Random(
        name="Склонения глагола",
        func=_get_verb_declentions,
        description="Поставьте глагол в нужное склонение:",
    ),
    Random(
        name="Глагол в прошедшем времени",
        func=lambda: _get_past_future_verb("Past"),
        description="Поставьте глагол в прошедшее время:",
    ),
    Random(
        name="Глагол в будущем времени",
        func=lambda: _get_past_future_verb("Future"),
        description="Поставьте глагол в будущее время:",
    ),
    Random(
        func=_get_noun,
        name="Существительное",
        description="Переведите существительное:",
    ),
    Random(
        func=_get_noun_plural,
        name="Существительное мн.ч.",
        description="Поставьте существительное во множественное число:",
    ),
    Random(
        func=_get_noun_dative,
        name="Дательный падеж",
        description="Поставьте существительное в дательный падеж:",
    ),
]

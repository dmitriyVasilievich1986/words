from main.models import Time, Declentions, Gender, Tags
from adjective.models import Adjective
from random import randint, choice
from pronoun.models import Pronoun
from django.db.models import Q
from verb.models import Verb
from noun.models import Noun
from typing import List

from .support_classes import (
    WordWithoutTranslate,
    WordBaseAnswerList,
    AnswerList,
    Random,
    Word,
    Base,
)


def _get_verb_declentions(**kwargs):
    declention = Declentions.objects.get(word="Nominative").id
    time = Time.objects.get(word="Present").id
    pronoun = Pronoun.random(declention=declention)
    verb = Verb.random(time=time, pronoun=pronoun, **kwargs)
    return WordBaseAnswerList(main=pronoun, secondary=verb)


def _get_past_future_verb(word, tags=None):
    time = Time.objects.get(word=word)
    verb = Verb.random(time=time)
    pronoun = verb.pronoun or Pronoun.random()
    verb_preposition = Verb.objects.get(time=time, base="", pronoun=pronoun)
    return AnswerList(
        WordWithoutTranslate(instance=pronoun),
        WordBaseAnswerList(main=verb_preposition, secondary=verb),
    )


def _get_noun(**kwargs):
    declention = Declentions.objects.get(word="Nominative").id
    noun = Noun.random(declention=declention, plural=False, **kwargs)
    return AnswerList(Word(instance=noun, hiden=True))


def _get_noun_plural(**kwargs):
    declention = Declentions.objects.get(word="Nominative").id
    noun = Noun.random(declention=declention, plural=True, **kwargs)
    if randint(0, 1):
        return AnswerList(Base(instance=noun))
    return AnswerList(Word(instance=noun, hiden=True))


def _all_noun_declentions(name, tags=None):
    verb = choice(
        Tags.objects.get(word=name).verb.filter(time=Time.objects.get(word="Present"))
    )
    preposition = (
        Word(choice(verb.preposition.all())) if verb.preposition.count() else None
    )

    declention = Declentions.objects.get(word=name)
    plural = bool(randint(0, 1))
    gender = Gender.random()
    adjective = Adjective.random(declention=declention, gender=gender, plural=plural)
    noun = Noun.random(declention=declention, gender=gender, plural=plural)

    return AnswerList(
        WordWithoutTranslate(instance=verb.pronoun),
        WordWithoutTranslate(instance=verb),
        preposition,
        Base(instance=adjective)
        if randint(0, 1)
        else Word(instance=adjective, hiden=True),
        Base(instance=noun) if randint(0, 1) else Word(instance=noun, hiden=True),
    )


def _get_verb(**kwargs):
    verb = Verb.random(pronoun=None, time=None, **kwargs)
    return AnswerList(Word(instance=verb, hiden=True))


RANDOM_CHOICES: List[Random] = [
    Random(
        name="Глагол",
        func=_get_verb,
        description="Переведите глагол:",
        tags=lambda: Q(verb__in=Verb.objects.filter(pronoun=None, time=None)),
    ),
    Random(
        name="Склонения глагола",
        func=_get_verb_declentions,
        description="Поставьте глагол в нужное склонение:",
        tags=lambda: Q(verb__in=Verb.objects.all()),
    ),
    Random(
        name="Глагол в прошедшем времени",
        func=lambda **kwargs: _get_past_future_verb("Past"),
        description="Поставьте глагол в прошедшее время:",
        tags=lambda: Q(pk=None),
    ),
    Random(
        name="Глагол в будущем времени",
        func=lambda **kwargs: _get_past_future_verb("Future"),
        description="Поставьте глагол в будущее время:",
        tags=lambda: Q(pk=None),
    ),
    Random(
        func=_get_noun,
        name="Существительное",
        description="Переведите существительное:",
        tags=lambda: Q(noun__in=Noun.objects.all()),
    ),
    Random(
        func=_get_noun_plural,
        name="Существительное мн.ч.",
        description="Поставьте существительное во множественное число:",
        tags=lambda: Q(noun__in=Noun.objects.all()),
    ),
    Random(
        name="Дательный падеж",
        func=lambda **kwargs: _all_noun_declentions("Dative"),
        description="Поставьте существительное и прилагательное в дательный падеж (Коме? Чему?):",
        tags=lambda: Q(pk=None),
    ),
    Random(
        name="Местный падеж",
        func=lambda **kwargs: _all_noun_declentions("Locative"),
        description="Поставьте существительное и прилагательное в местный падеж (О коме? О чему?):",
        tags=lambda: Q(pk=None),
    ),
    Random(
        name="Родительный падеж",
        func=lambda **kwargs: _all_noun_declentions("Genitive"),
        description="Поставьте существительное и прилагательное в родительный падеж (Кога? Чега?):",
        tags=lambda: Q(pk=None),
    ),
    Random(
        name="Винительный падеж",
        func=lambda **kwargs: _all_noun_declentions("Accusative"),
        description="Поставьте существительное и прилагательное в винительный падеж (Кога? Шта?):",
        tags=lambda: Q(pk=None),
    ),
    Random(
        name="Инструментальный падеж",
        func=lambda **kwargs: _all_noun_declentions("Instrumental"),
        description="Поставьте существительное и прилагательное в инструментальный падеж (С ким? Чиме?):",
        tags=lambda: Q(pk=None),
    ),
]

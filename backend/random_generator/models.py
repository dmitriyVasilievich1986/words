from main.models import Time, Declentions, Gender, Tags
from adjective.models import Adjective
from random import randint, choice
from pronoun.models import Pronoun
from verb.models import Verb
from noun.models import Noun

from .support_classes import (
    WordWithoutTranslate,
    WordBaseAnswerList,
    AnswerList,
    Random,
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
    time = Time.objects.get(word=word)
    verb = Verb.random(time=time)
    pronoun = verb.pronoun or Pronoun.random()
    verb_preposition = Verb.objects.get(time=time, base="", pronoun=pronoun)
    return AnswerList(
        WordWithoutTranslate(instance=pronoun),
        WordBaseAnswerList(main=verb_preposition, secondary=verb),
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


def _all_noun_declentions(name):
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
        name="Дательный падеж",
        func=lambda: _all_noun_declentions("Dative"),
        description="Поставьте существительное и прилагательное в дательный падеж (Коме? Чему?):",
    ),
    Random(
        name="Местный падеж",
        func=lambda: _all_noun_declentions("Locative"),
        description="Поставьте существительное и прилагательное в местный падеж (О коме? О чему?):",
    ),
    Random(
        name="Родительный падеж",
        func=lambda: _all_noun_declentions("Genitive"),
        description="Поставьте существительное и прилагательное в родительный падеж (Кога? Чега?):",
    ),
    Random(
        name="Винительный падеж",
        func=lambda: _all_noun_declentions("Accusative"),
        description="Поставьте существительное и прилагательное в винительный падеж (Кога? Шта?):",
    ),
    Random(
        name="Инструментальный падеж",
        func=lambda: _all_noun_declentions("Instrumental"),
        description="Поставьте существительное и прилагательное в инструментальный падеж (С ким? Чиме?):",
    ),
]

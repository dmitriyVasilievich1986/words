from main.models import Time, Declentions, Gender, Tags, Infinitive, PartsOfSpeech
from pronoun.models import Pronoun, PersonalPronoun
from dataclasses import dataclass, asdict
from adjective.models import Adjective
from random import randint, choice
from typing import List, Optional
from django.db.models import Q
from verb.models import Verb
from noun.models import Noun
from django.db import models
from abc import ABC

from .support_classes import (
    WordWithoutTranslate,
    WordBaseAnswerList,
    AnswerList,
    Random,
    Word,
    Base,
)

class RulesRandom(models.Model):
    description = models.CharField(max_length=150, blank=False, null=False)
    name = models.CharField(max_length=150, blank=False, null=False)

@dataclass
class RandomResponse:
    translate: str
    word: str

    base: Optional[str] = None
    hint: Optional[str] = None

    def __post_init__(self):
        if self.base is None:
            self.base = self.word
        elif self.base != "" and self.base != self.word:
            index = next((i for i in range(min(len(self.word), len(self.base))) if self.word[i]!=self.base[i]), float("inf"))
            self.base = self.word[:min(index, len(self.word) - 1)]

class IRandom(ABC):
    def _form_response(self) -> list[RandomResponse]:
        raise NotImplementedError

    def get_data(self) -> list[dict]:
        return [asdict(x) for x in self._form_response()]

class VerbRandom(IRandom):
    def __init__(self, cache={"infinitive": 1}):
        self.part_of_speech = PartsOfSpeech.objects.get(word="verb")
        self.infinitive = choice(Infinitive.objects.filter(part_of_speech=self.part_of_speech).exclude(id=cache["infinitive"]).all())

        cache["infinitive"] = self.infinitive.id
    
    def _form_response(self):
        return [
            RandomResponse(
                translate=self.infinitive.translate,
                word=self.infinitive.word,
                base="",
            )
        ]

class VerbInflectionRandom(IRandom):
    def __init__(self, cache={"personal_pronoun": 1, "verb": 1}):
        self.personal_pronoun = choice(PersonalPronoun.objects.exclude(verb__isnull=True, id=cache["personal_pronoun"]).all())
        self.verb = choice(Verb.objects.filter(personal_pronoun=self.personal_pronoun).exclude(id=cache["verb"]).all())
        
        cache["personal_pronoun"] = self.personal_pronoun.id
        cache["verb"] = self.verb.id

    def _form_response(self):
        return [
            RandomResponse(
                translate=self.personal_pronoun.translate,
                word=self.personal_pronoun.word,
            ),
            RandomResponse(
                base=self.verb.infinitive.word,
                translate=self.verb.translate,
                word=self.verb.word,
            )
        ]


def _get_verb_declentions(**kwargs):
    declention = Declentions.objects.get(word="Nominative").id
    time = Time.objects.get(word="Present").id
    pronoun = Pronoun.random(declention=declention)
    verb = Verb.random(time=time, pronoun=pronoun, **kwargs)
    return WordBaseAnswerList(main=pronoun, secondary=verb)


def _get_past_future_verb(word, **kwargs):
    time = Time.objects.get(word=word)
    verb = Verb.random(time=time, **kwargs)
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
        tags=lambda: Q(verb__in=Verb.objects.all()),
        count=lambda: Verb._get_objects().values("base").distinct().count(),
    ),
    Random(
        name="Склонения глагола",
        func=_get_verb_declentions,
        tags=lambda: Q(verb__in=Verb.objects.all()),
        description="Поставьте глагол в нужное склонение:",
        count=lambda: Verb._get_objects().values("base").distinct().count(),
    ),
    Random(
        name="Глагол в прошедшем времени",
        tags=lambda: Q(verb__in=Verb.objects.all()),
        description="Поставьте глагол в прошедшее время:",
        func=lambda **kwargs: _get_past_future_verb("Past"),
        count=lambda: Verb._get_objects().values("base").distinct().count(),
    ),
    Random(
        name="Глагол в будущем времени",
        tags=lambda: Q(verb__in=Verb.objects.all()),
        description="Поставьте глагол в будущее время:",
        func=lambda **kwargs: _get_past_future_verb("Future"),
        count=lambda: Verb._get_objects().values("base").distinct().count(),
    ),
    Random(
        func=_get_noun,
        name="Существительное",
        description="Переведите существительное:",
        tags=lambda: Q(noun__in=Noun.objects.all()),
        count=lambda: Noun._get_objects()
        .filter(plural=False)
        .values("base")
        .distinct()
        .count(),
    ),
    Random(
        func=_get_noun_plural,
        name="Существительное мн.ч.",
        tags=lambda: Q(noun__in=Noun.objects.all()),
        description="Поставьте существительное во множественное число:",
        count=lambda: Noun._get_objects()
        .filter(plural=True)
        .values("base")
        .distinct()
        .count(),
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

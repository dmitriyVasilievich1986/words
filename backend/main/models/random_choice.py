from .pronoun_models import PersonalPronoun, Pronoun
from .noun_models import NounInfinitive, Noun
from .declentions_models import Declentions
from .verb_models import VerbInfinitive
from random import randint, choice
from .gender_models import Gender
from dataclasses import dataclass
from .time_models import Time
from enum import Enum, auto
from typing import Any
import re


@dataclass
class RandomChoice:
    name: str
    random: Any
    description: str

    def json(self):
        return {
            "name": self.name,
            "description": self.description,
        }


class WordPart(Enum):
    postfix = auto()
    full = auto()
    base = auto()


class Answer(dict):
    def __init__(
        self, instance: VerbInfinitive = None, hiden=False, part=WordPart.full
    ):
        if part is WordPart.base:
            self["hiden"] = False
            self["word"] = getattr(instance, "base", " ")
            self["translate"] = getattr(instance, "translate", " ")
        elif part is WordPart.postfix:
            self["hiden"] = True
            self["translate"] = ""
            b = getattr(instance, "base", "")
            self["word"] = re.sub(r"^" + b, "", getattr(instance, "word", ""))
        else:
            self["hiden"] = hiden
            self["word"] = getattr(instance, "word", " ")
            self["translate"] = getattr(instance, "translate", " ")


def get_base_postfix(word):
    return [
        Answer(instance=word, part=WordPart.base),
        Answer(instance=word, part=WordPart.postfix),
    ]


def personal_pron_verb(**kwargs):
    pp = PersonalPronoun._random()
    vi = VerbInfinitive._random()
    t = kwargs.pop("time", Time.objects.first().id)
    v = vi.verb.get(pronoun=pp.id, time=t)
    if randint(0, 1):
        return [
            Answer(pp, hiden=False),
            Answer(),
            *get_base_postfix(v),
        ]
    ch = randint(1, 3)
    return [
        Answer(pp, hiden=bool(ch & 1)),
        Answer(),
        Answer(v, hiden=bool(ch & 2)),
    ]


def noun_plural(**kwargs):
    n = NounInfinitive._random(**kwargs).noun.get(plural=True)
    if randint(0, 1):
        return get_base_postfix(n)
    return [Answer(n, hiden=True)]


def pron_noun(**kwargs):
    g = Gender._random()
    pl = bool(randint(0, 1))
    d = Declentions._random()
    p = Pronoun._random(gender=g.id, plural=pl, declentions=d, **kwargs)
    n = NounInfinitive._random(gender=g.id).noun.get(plural=pl, declention=d, **kwargs)

    if randint(0, 1):
        ch = randint(1, 3)
        return [
            Answer(p, hiden=bool(ch & 1)),
            Answer(),
            Answer(n, hiden=bool(ch & 2)),
        ]
    return [
        Answer(p),
        Answer(),
        *get_base_postfix(n),
    ]


RANDOM_CHOICES = [
    RandomChoice(
        random=lambda **k: [Answer(hiden=True, instance=VerbInfinitive._random(**k))],
        description="Только глагол",
        name="Глагол",
    ),
    RandomChoice(
        name="Личное местоимение + Глагол",
        description="Только глагол",
        random=personal_pron_verb,
    ),
    RandomChoice(
        description="Существительное",
        random=lambda **k: [Answer(hiden=True, instance=NounInfinitive._random(**k))],
        name="Существительное",
    ),
    RandomChoice(
        description="Существительное множественное число",
        name="Существительное мн.ч.",
        random=noun_plural,
    ),
    RandomChoice(
        description="Местоимение + существительное",
        name="Местоимение + существительное",
        random=pron_noun,
    ),
]

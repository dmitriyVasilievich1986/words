from .noun_models import NounInfinitive, Noun
from .pronoun_models import PersonalPronoun
from .verb_models import VerbInfinitive
from dataclasses import dataclass
from .time_models import Time
from random import randint
from typing import Any


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


class Answer(dict):
    def __init__(
        self, instance: VerbInfinitive = None, hiden=False, base=False, end=False
    ):
        if base:
            self["translate"] = getattr(instance, "translate", " ")
            self["word"] = getattr(instance, "base", " ")
        elif end:
            self["word"] = getattr(instance, "word", "").lstrip(
                getattr(instance, "base", "")
            )
            self["translate"] = ""
        else:
            self["translate"] = getattr(instance, "translate", " ")
            self["word"] = getattr(instance, "word", " ")
        self["hiden"] = hiden


def personal_pron_verb(**kwargs):
    pp = PersonalPronoun._random()
    vi = VerbInfinitive._random()
    t = kwargs.pop("time", Time.objects.first().id)
    v = vi.verb.get(pronoun=pp.id, time=t)
    if randint(0, 1):
        return [
            Answer(pp, hiden=bool(randint(0, 1))),
            Answer(),
            Answer(v, hiden=False, base=True),
            Answer(v, hiden=True, end=True),
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
        return [
            Answer(n, hiden=False, base=True),
            Answer(n, hiden=True, end=True),
        ]
    return [Answer(n, hiden=True)]


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
]

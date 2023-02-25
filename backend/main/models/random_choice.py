from .verb_models import VerbInfinitive, Verb
from .pronoun_models import PersonalPronoun
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
    else:
        return [
            Answer(pp, hiden=bool(randint(0, 1))),
            Answer(),
            Answer(v, hiden=bool(randint(0, 1))),
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
]

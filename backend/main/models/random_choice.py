from .verb_models import VerbInfinitive, Verb
from .pronoun_models import PersonalPronoun
from dataclasses import dataclass
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
    def __init__(self, instance: VerbInfinitive = None, hiden=False):
        self["translate"] = getattr(instance, "translate", " ")
        self["word"] = getattr(instance, "word", " ")
        self["hiden"] = hiden

        if hasattr(instance, "base"):
            self["base"] = instance.base


def personal_pron_verb(**kwargs):
    pp = PersonalPronoun._random()
    vi = VerbInfinitive._random()
    t = kwargs.pop("time", 1)
    v = vi.verb.get(pronoun=pp.id, time=t)
    return [
        Answer(pp, hiden=True),
        Answer(),
        Answer(v, hiden=True),
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

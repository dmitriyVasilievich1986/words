from .verb_models import VerbInfinitive, Verb
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


RANDOM_CHOICES = [
    RandomChoice(
        random=lambda **k: [Answer(hiden=True, instance=VerbInfinitive._random(**k))],
        description="Только глагол",
        name="Глагол",
    ),
]

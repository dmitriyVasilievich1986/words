from dataclasses import dataclass
from typing import Callable
from random import randint
import re

from main.models import Time, Declentions
from pronoun.models import Pronoun
from verb.models import Verb
from noun.models import Noun


class Answer(dict):
    def __init__(self, word, translate="", hiden=False):
        self["translate"] = translate
        self["hiden"] = hiden
        self["word"] = word


class Word(list):
    def __init__(self, instance, hiden=False):
        self.append(
            Answer(word=instance.word, translate=instance.translate, hiden=hiden)
        )


class Empty(list):
    def __init__(self):
        self.append(Answer(word=" ", translate=" "))


class Base(list):
    def __init__(self, instance):
        base = instance.base
        word = re.sub(r"^" + base, "", instance.word)

        self.append(Answer(word=base, translate=instance.translate))
        self.append(Answer(word=word, hiden=True))


class AnswerList(list):
    def __init__(self, *args):
        for index, answer in enumerate(args, start=1):
            self.extend(answer)
            if len(args) > index:
                self.extend(Empty())


@dataclass
class Random:
    func: Callable
    name: str

    def json(self) -> dict:
        return {"name": self.name, "word": self.name}

    def __call__(self) -> AnswerList:
        return self.func()


def _get_rand_from_three():
    ch = randint(1, 3)
    return bool(ch & 1), bool(ch & 2)


def _get_verb():
    declention = Declentions.objects.get(word="Nominative").id
    time = Time.objects.get(word="Present").id
    pronoun = Pronoun.random(declention=declention)
    if randint(0, 1):
        return AnswerList(
            Word(instance=pronoun),
            Base(instance=Verb.random(time=time, pronoun=pronoun)),
        )
    first, second = _get_rand_from_three()
    return AnswerList(
        Word(instance=pronoun, hiden=first),
        Word(instance=Verb.random(time=time, pronoun=pronoun), hiden=second),
    )


def _get_noun():
    declention = Declentions.objects.get(word="Nominative").id
    noun = Noun.random(declention=declention)
    return AnswerList(Word(instance=noun, hiden=True))


RANDOM_CHOICES = [
    Random(name="Глагол", func=_get_verb),
    Random(name="Существительное", func=_get_noun),
]

from dataclasses import dataclass
from typing import Callable
import re


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
    name: str
    func: Callable
    description: str = ""

    def json(self) -> dict:
        return {
            "name": self.name,
            "word": self.name,
            "description": self.description,
        }

    def __call__(self) -> AnswerList:
        return self.func()

from dataclasses import dataclass
from typing import Callable
from random import randint
import re


def _get_rand_from_three():
    ch = randint(1, 3)
    return bool(ch & 1), bool(ch & 2)


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


class WordWithoutTranslate(list):
    def __init__(self, instance, hiden=False):
        self.append(Answer(word=instance.word, translate=instance.word, hiden=hiden))


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
            if answer is None or isinstance(answer, Empty):
                continue
            self.extend(answer)
            if len(args) > index:
                self.extend(Empty())


class WordMainSecondary(AnswerList):
    def __init__(self, main, secondary):
        first, second = _get_rand_from_three()
        super().__init__(
            Word(instance=main, hiden=first),
            Word(instance=secondary, hiden=second),
        )


class WordBaseAnswerList(AnswerList):
    def __init__(self, main, secondary):
        if randint(0, 1):
            super().__init__(
                Word(instance=main),
                Base(instance=secondary),
            )
        else:
            self.extend(WordMainSecondary(main, secondary))


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

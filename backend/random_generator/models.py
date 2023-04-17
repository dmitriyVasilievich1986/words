from .support_classes import Answer, AnswerList, Word, Empty, Base, Random
from main.models import Time, Declentions
from pronoun.models import Pronoun
from verb.models import Verb
from noun.models import Noun
from random import randint


def _get_rand_from_three():
    ch = randint(1, 3)
    return bool(ch & 1), bool(ch & 2)


def _get_verb_declentions():
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
        func=_get_noun,
        name="Существительное",
        description="Переведите существительное:",
    ),
]

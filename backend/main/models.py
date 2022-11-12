from django.db import models


# Create your models here.
class Case(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)


class Noun(models.Model):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)


class NounCase(models.Model):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)

    noun = models.ForeignKey(
        related_name="noun_case",
        on_delete=models.CASCADE,
        to="Noun",
    )
    case = models.ForeignKey(
        related_name="noun_case",
        on_delete=models.CASCADE,
        to="Case",
    )


class Pron(models.Model):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)


class Verb(models.Model):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)


class VerbDeclension(models.Model):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)

    verb = models.ForeignKey(
        related_name="verb_declentions",
        on_delete=models.CASCADE,
        to="Verb",
    )
    pron = models.ForeignKey(
        related_name="verb_declentions",
        on_delete=models.CASCADE,
        to="Pron",
    )


def input():
    words = [
        [
            {"word": "книга", "translate": "книга"},
            {"word": "книгу", "translate": "книгу"},
        ],
        [
            {"word": "река", "translate": "река"},
            {"word": "реку", "translate": "реку"},
        ],
    ]
    for noun, nc in words:
        n = Noun(**noun)
        n.save()
        NounCase(noun=n, case=Case.objects.get(name="accusative"), **nc).save()

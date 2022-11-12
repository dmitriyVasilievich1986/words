from django.db import models


# Create your models here.
class Case(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)


class Adjective(models.Model):
    gender = models.CharField(max_length=150, blank=False, null=False, default="f")
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)


class Noun(models.Model):
    gender = models.CharField(max_length=150, blank=False, null=False, default="f")
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


class AdjCase(models.Model):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)

    adjective = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="adj_case",
        to="Adjective",
    )
    case = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="adj_case",
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


def i():
    words = [
        [
            {"word": "лепа", "translate": "красивая"},
            {"word": "лепу", "translate": "красивую"},
        ],
    ]
    for noun, nc in words:
        n = Adjective(**noun)
        n.save()
        AdjCase(adjective=n, case=Case.objects.get(name="accusative"), **nc).save()

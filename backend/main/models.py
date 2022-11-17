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

    @property
    def gender(self):
        return self.noun.gender


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

    @property
    def gender(self):
        return self.adjective.gender


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

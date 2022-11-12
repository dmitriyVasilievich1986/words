from django.db import models
from random import choices
from enum import Enum


Pronoun = {
    "ja": "я",
    "ti": "ти",
    "on": "он",
    "vi": "ви",
    "mi": "ми",
    "oni": "они",
}


# Create your models here.
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

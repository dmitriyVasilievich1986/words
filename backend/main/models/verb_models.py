from .pron_models import Pron
from django.db import models


class Verb(models.Model):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)


class VerbDeclension(models.Model):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)

    verb = models.ForeignKey(
        related_name="verb_declentions",
        on_delete=models.CASCADE,
        to=Verb,
    )
    pron = models.ForeignKey(
        related_name="verb_declentions",
        on_delete=models.CASCADE,
        to=Pron,
    )

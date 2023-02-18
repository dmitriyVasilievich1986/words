from .declentions_models import Declentions
from .pronoun_models import PersonalPronoun
from .random_mixin import RandomMixin
from django.db import models


class VerbInfinitive(models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)


class Verb(models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)
    plural = models.BooleanField(default=False)

    infinitive = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="verb",
        to=VerbInfinitive,
        null=True,
    )
    declention = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="verb",
        to=Declentions,
        null=True,
    )
    pronoun = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="verb",
        to=PersonalPronoun,
        null=True,
    )

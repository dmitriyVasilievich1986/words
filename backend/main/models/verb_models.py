from .pronoun_models import PersonalPronoun
from .random_mixin import RandomMixin
from .time_models import Time
from django.db import models


class VerbInfinitive(models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)
    base = models.CharField(max_length=150, blank=False, null=False)


class Verb(models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)

    infinitive = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="verb",
        to=VerbInfinitive,
        null=True,
    )
    time = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="verb",
        null=True,
        to=Time,
    )
    pronoun = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="verb",
        to=PersonalPronoun,
        null=True,
    )

    @property
    def base(self):
        return self.infinitive.base

from .random_mixin import RandomMixin
from .gender_models import Gender
from django.db import models


class PersonalPronoun(models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)
    plural = models.BooleanField(default=False)


class Pronoun(models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)
    plural = models.BooleanField(default=False)

    gender = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="pronoun",
        to=Gender,
        null=True,
    )

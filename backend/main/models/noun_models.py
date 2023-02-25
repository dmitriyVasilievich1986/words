from .declentions_models import Declentions
from .random_mixin import RandomMixin
from .gender_models import Gender
from django.db import models


class NounInfinitive(models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)
    base = models.CharField(max_length=150, blank=False, null=False)


class Noun(models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)
    plural = models.BooleanField(default=False)

    infinitive = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="noun",
        to=NounInfinitive,
        null=True,
    )
    declention = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="noun",
        to=Declentions,
        null=True,
    )
    gender = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="noun",
        to=Gender,
        null=True,
    )

    @property
    def base(self):
        return self.infinitive.base

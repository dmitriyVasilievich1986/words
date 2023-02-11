from .case_models import Case
from django.db import models


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
        to=Noun,
    )
    case = models.ForeignKey(
        related_name="noun_case",
        on_delete=models.CASCADE,
        to=Case,
    )

    @property
    def gender(self):
        return self.noun.gender

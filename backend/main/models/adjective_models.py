from .case_models import Case
from django.db import models


class Adjective(models.Model):
    gender = models.CharField(max_length=150, blank=False, null=False, default="f")
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)


class AdjCase(models.Model):
    gender = models.CharField(max_length=150, blank=False, null=False, default="f")
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)

    adjective = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="adj_case",
        to=Adjective,
    )
    case = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="adj_case",
        to=Case,
    )

from django.db import models


class Pronoun(models.Model):
    gender = models.CharField(max_length=150, blank=False, null=False, default="f")
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)

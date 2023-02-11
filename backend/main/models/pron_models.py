from django.db import models


class Pron(models.Model):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)

from django.db import models


class Case(models.Model):
    name = models.CharField(max_length=150, blank=False, null=False)

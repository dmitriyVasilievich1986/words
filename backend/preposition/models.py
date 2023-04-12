from main.support_mixin import RandomMixin, RepresentationClass
from django.db import models


class Preposition(RepresentationClass, models.Model, RandomMixin):
    translate = models.CharField(max_length=50, blank=False, null=False)
    word = models.CharField(max_length=50, blank=False, null=False)

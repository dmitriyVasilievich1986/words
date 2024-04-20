from .support_mixin import RandomMixin, RepresentationClass
from django.db import models


class Declentions(RepresentationClass, models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)


class Tags(RepresentationClass, models.Model, RandomMixin):
    word = models.CharField(max_length=150, blank=False, null=False, unique=True)
    hidden = models.BooleanField(default=True)


class Gender(RepresentationClass, models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)


class Time(RepresentationClass, models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)


class Preposition(RepresentationClass, models.Model, RandomMixin):
    translate = models.CharField(max_length=50, blank=False, null=False)
    word = models.CharField(max_length=50, blank=False, null=False)

class Base(models.Model):    
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)

    class Meta:
        abstract = True

class PartsOfSpeech(Base):
    pass

class Infinitive(Base):
    part_of_speech = models.ForeignKey(
        related_name="infinitive",
        on_delete=models.CASCADE,
        to=PartsOfSpeech,
        blank=False,
        null=False,
    )
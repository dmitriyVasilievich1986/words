from main.support_mixin import RepresentationBaseClass, RandomMixin
from main.models import Time, Tags, Preposition
from pronoun.models import Pronoun
from django.db.models import Q
from django.db import models
from functools import reduce


class Verb(RepresentationBaseClass, models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)
    base = models.CharField(max_length=150)

    preposition = models.ManyToManyField(
        related_name="verb",
        to=Preposition,
        blank=True,
    )
    tags = models.ManyToManyField(
        related_name="verb",
        blank=True,
        to=Tags,
    )
    pronoun = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="verb",
        to=Pronoun,
        null=True,
    )
    time = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="verb",
        null=True,
        to=Time,
    )

    def __repr__(self) -> str:
        pronoun = self.pronoun and f"Pronoun: <<{self.pronoun}>>"
        time = self.time and f"Time: <<{self.time}>>"

        return super().__repr__(time, pronoun)

    @classmethod
    def _get_objects(cls, tags=None):
        tags = tags or list()
        return cls.objects.filter(
            reduce(lambda a, b: a | Q(tags=b), [Q(), *tags])
        ).filter(~Q(base=""))

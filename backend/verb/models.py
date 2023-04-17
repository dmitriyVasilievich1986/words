from main.support_mixin import RepresentationBaseClass, RandomMixin
from pronoun.models import Pronoun
from django.db.models import Q
from main.models import Time
from django.db import models


class Verb(RepresentationBaseClass, models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)
    base = models.CharField(max_length=150)

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
    def _get_objects(cls):
        return cls.objects.filter(~Q(base=""))

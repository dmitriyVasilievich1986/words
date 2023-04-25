from main.support_mixin import RandomMixin, RepresentationBaseClass
from main.models import Declentions, Gender, Preposition, Tags
from django.db import models


class Noun(RepresentationBaseClass, models.Model, RandomMixin):
    translate = models.CharField(max_length=150, blank=False, null=False)
    word = models.CharField(max_length=150, blank=False, null=False)
    base = models.CharField(max_length=50, blank=False, null=True)
    plural = models.BooleanField(default=False)

    tags = models.ManyToManyField(
        related_name="noun",
        blank=True,
        to=Tags,
    )
    prepositions = models.ManyToManyField(
        related_name="noun",
        to=Preposition,
        blank=True,
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

    def __repr__(self) -> str:
        plural = f"Plural: {self.plural}"
        gender = self.gender and f"Gender: <<{self.gender}>>"
        declention = self.declention and f"Declention: <<{self.declention}>>"
        preposition = (
            self.prepositions and f"Prepositions: <<{self.prepositions.all()}>>"
        )
        return super().__repr__(plural, gender, declention, preposition)

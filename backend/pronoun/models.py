from main.support_mixin import RandomMixin, RepresentationClass
from main.models import Declentions
from django.db import models
from main.models import Base


class Pronoun(RepresentationClass, models.Model, RandomMixin):
    translate = models.CharField(max_length=50, blank=False, null=False)
    word = models.CharField(max_length=50, blank=False, null=False)
    plural = models.BooleanField(default=False)

    declention = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="pronoun",
        to=Declentions,
        null=True,
    )

    def __repr__(self):
        declention = self.declention and f"Declentions: {self.declention}"
        return super().__repr__(declention)

class PersonalPronoun(Base):
    pass
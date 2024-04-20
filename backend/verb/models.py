from pronoun.models import PersonalPronoun
from main.models import Base, Infinitive
from django.db import models


class Verb(Base):
    infinitive = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="verb",
        to=Infinitive,
        blank=False,
        null=False,
    )
    personal_pronoun = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name="verb",
        to=PersonalPronoun,
        blank=False,
        null=False,
    )

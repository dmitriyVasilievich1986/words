from django.db.models import Q
from random import choice


class RandomMixin:
    @classmethod
    def _random(cls, cache=[None], **kwargs):
        objects = cls.objects.all()
        if not objects.count():
            return None
        instance = choice(
            objects.filter(**kwargs).filter(
                ~Q(id=cache[0] if objects.count() > 1 else None)
            )
        )
        cache[0] = instance.id
        return instance

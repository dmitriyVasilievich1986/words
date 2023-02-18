from django.db.models import Q
from random import choice


class RandomMixin:
    @classmethod
    def _random(cls, cache=[None], **kwargs):
        objects = cls.objects.filter(**kwargs)
        if objects.count() <= 1:
            return objects.first()
        instance = choice(objects.filter(~Q(id=cache[0])))
        cache[0] = instance.id
        return instance

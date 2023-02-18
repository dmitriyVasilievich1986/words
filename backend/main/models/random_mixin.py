from django.db.models import Q
from random import choice


class RandomMixin:
    @classmethod
    def _random(cls, cache={}, **kwargs):
        objects = cls.objects.filter(**kwargs)
        if objects.count() <= 1:
            cache[cls.__name__] = None
            return objects.first()
        instance = choice(objects.filter(~Q(id=cache.get(cls.__name__))))
        cache[cls.__name__] = instance.id
        return instance

from django.db.models import Q
from random import choice


class RepresentationClass:
    translate = None
    word = None
    id = None

    def __repr__(self, *args) -> str:
        id_ = f"ID: {self.id}"
        word = f"ID: {self.word}"
        translate = f"ID: {self.translate}"
        return ", ".join(filter(bool, (id_, word, translate, *args)))

    def __str__(self) -> str:
        return self.__repr__()


class RepresentationBaseClass(RepresentationClass):
    base = None

    def __repr__(self, *args) -> str:
        base = self.base and f"Base: {self.base}"
        return super().__repr__(base, *args)


class RandomMixin:
    @classmethod
    def random(cls, cache={}, **kwargs):
        objects = cls._get_objects().filter(**kwargs)
        if objects.count() <= 1:
            cache[cls.__name__] = None
            return objects.first()
        instance = choice(objects.filter(~Q(id=cache.get(cls.__name__))))
        cache[cls.__name__] = instance.id
        return instance

    @classmethod
    def _get_objects(cls):
        return cls.objects.all()

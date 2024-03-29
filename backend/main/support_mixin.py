from django.db.models import Q
from random import choice


class RDict(dict):
    def __init__(self, params):
        self["id"] = params.id
        self["word"] = params.word


class RepresentationClass:
    translate = None
    word = None
    id = None

    def __repr__(self, *args) -> str:
        id_ = f"ID: {self.id}"
        word = f"Word: {self.word}"
        translate = f"Translate: {self.translate}"
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
    def random(cls, cache={}, tags=None, **kwargs):
        objects = cls._get_objects(tags=tags).filter(**kwargs)
        if objects.count() <= 1:
            cache[cls.__name__] = None
            return objects.first()
        instance = choice(objects.filter(~Q(id=cache.get(cls.__name__))))
        cache[cls.__name__] = instance.id
        return instance

    @classmethod
    def _get_objects(cls, **kwargs):
        return cls.objects.all()

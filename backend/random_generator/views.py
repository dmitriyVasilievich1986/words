from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from .models import RANDOM_CHOICES
from django.db.models import Q
from main.models import Tags
from functools import reduce
from random import choice
from operator import or_
import json
from django.core.exceptions import ObjectDoesNotExist

from .models import RulesRandom
from .serializer import RulesRandomSerializer

from .models import (
    VerbInflectionRandom,
    VerbRandom,
)

class RulesRandomViewSet(ReadOnlyModelViewSet):
    serializer_class = RulesRandomSerializer
    queryset = RulesRandom.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.name == "Глагол":
            return Response(VerbRandom().get_data())
        if instance.name == "Склонение глагола":
            return Response(VerbInflectionRandom().get_data())
        raise ObjectDoesNotExist()


class RandomChoicesViewSet(GenericViewSet):
    last_choice_list = list()
    last_tags = list()

    def create(self, request, *args, **kwargs):
        body = json.loads(request.body)
        random_choices = body["random_choices"]
        tags = body["params"]["tags"]
        self._get_tags(random_choices, tags)
        choice_id = choice(self.last_choice_list)
        return Response(
            {
                "answer_list": RANDOM_CHOICES[choice_id](**body.get("params", dict())),
                "tags": self.last_tags,
            }
        )

    def _get_tags(self, random_choices, tags):
        if not self.last_tags or set(random_choices) != set(self.last_choice_list):
            tags_filter = reduce(
                or_, [RANDOM_CHOICES[x].tags() for x in random_choices]
            )
            self.last_tags = [
                {"id": x.id, "word": x.word}
                for x in Tags.objects.filter(hidden=False)
                .filter(tags_filter)
                .distinct()
            ]
            self.last_choice_list = [
                x
                for x in random_choices
                if not tags
                or Tags.objects.filter(
                    RANDOM_CHOICES[x].tags() & Q(id__in=tags)
                ).count()
            ]
        return self.last_tags, self.last_choice_list

    def list(self, request, *args, **kwargs):
        return Response([{"id": i, **x.json()} for i, x in enumerate(RANDOM_CHOICES)])

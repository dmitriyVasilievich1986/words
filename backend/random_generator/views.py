from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import exceptions
from .models import RANDOM_CHOICES


class RandomChoicesViewSet(GenericViewSet):
    def retrieve(self, request, pk, *args, **kwargs):
        if int(pk) >= len(RANDOM_CHOICES):
            raise exceptions.NotFound
        return Response(
            RANDOM_CHOICES[int(pk)](
                **{k: request.GET[k] for k in dict(request.GET).keys()}
            )
        )

    def list(self, request, *args, **kwargs):
        return Response([{"id": i, **x.json()} for i, x in enumerate(RANDOM_CHOICES)])

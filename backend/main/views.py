from .models import Pron, Verb, VerbDeclension, Noun, Case, NounCase, Adjective, AdjCase
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializer import (
    VerbDeclensionSerializer,
    PronSerializer,
    VerbSerializer,
    NounCaseSerializer,
    NounSerializer,
    CaseSerializer,
    AdjectiveSerializer,
    AdjCaseSerializer,
)


class AdjCaseViewSet(ModelViewSet):
    serializer_class = AdjCaseSerializer
    queryset = AdjCase.objects.all()


class AdjectiveViewSet(ModelViewSet):
    serializer_class = AdjectiveSerializer
    queryset = Adjective.objects.all()


class NounCaseViewSet(ModelViewSet):
    serializer_class = NounCaseSerializer
    queryset = NounCase.objects.all()

    @action(detail=False, methods=["POST"])
    def bulk(self, request, *args, **kwargs):
        n = NounSerializer(data=request.data["noun"])
        n.is_valid(raise_exception=True)
        n.save()
        print(n.data)
        for x in request.data["case_noun"]:
            c = Case.objects.get(id=x["case"])
            c = CaseSerializer(instance=c)
            vd = NounCaseSerializer(
                data={"noun": n.instance.id, **x, "case": c.instance.id}
            )
            vd.is_valid(raise_exception=True)
            vd.save()
            print(vd.data)
        return Response(n.data)


class CaseViewSet(ModelViewSet):
    serializer_class = CaseSerializer
    queryset = Case.objects.all()


class NounViewSet(ModelViewSet):
    serializer_class = NounSerializer
    queryset = Noun.objects.all()


class PronViewSet(ModelViewSet):
    serializer_class = PronSerializer
    queryset = Pron.objects.all()


class VerbViewSet(ModelViewSet):
    serializer_class = VerbSerializer
    queryset = Verb.objects.all()


class VerbDeclensionViewSet(ModelViewSet):
    serializer_class = VerbDeclensionSerializer
    queryset = VerbDeclension.objects.all()

    @action(detail=False, methods=["POST"])
    def bulk(self, request, *args, **kwargs):
        v = VerbSerializer(data=request.data["verb"])
        v.is_valid(raise_exception=True)
        v.save()
        print(v.data)
        for x in request.data["verb_pron"]:
            p = Pron.objects.get(id=x["pron"])
            p = PronSerializer(instance=p)
            vd = VerbDeclensionSerializer(
                data={"verb": v.instance.id, **x, "pron": p.instance.id}
            )
            vd.is_valid(raise_exception=True)
            vd.save()
            print(vd.data)
        return Response(v.data)

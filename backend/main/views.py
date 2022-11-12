from django.shortcuts import render
from rest_framework.response import Response
from .models import Verb, VerbDeclension, Pronoun
from random import choice
from django.http.response import HttpResponse


def index_view(request):
    ch = choice(choice(Verb.objects.all()).verb_declentions.all())
    pron = ch.pron.word
    verb = ch.word
    return HttpResponse(f"{pron} {verb}")

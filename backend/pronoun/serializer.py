from rest_framework.serializers import ModelSerializer
from .models import Pronoun, PersonalPronoun


class PronounSerializer(ModelSerializer):
    class Meta:
        model = Pronoun
        fields = "__all__"

class PersonalPronounSerializer(ModelSerializer):
    class Meta:
        model = PersonalPronoun
        fields = "__all__"

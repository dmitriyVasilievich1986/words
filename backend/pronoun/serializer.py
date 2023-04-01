from rest_framework.serializers import ModelSerializer
from .models import Pronoun


class PronounSerializer(ModelSerializer):
    class Meta:
        model = Pronoun
        fields = "__all__"

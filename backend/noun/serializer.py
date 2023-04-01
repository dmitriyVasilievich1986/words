from rest_framework.serializers import ModelSerializer
from .models import Noun


class NounSerializer(ModelSerializer):
    class Meta:
        model = Noun
        fields = "__all__"

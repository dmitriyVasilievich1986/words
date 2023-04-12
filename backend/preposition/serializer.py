from rest_framework.serializers import ModelSerializer
from .models import Preposition


class PrepositionSerializer(ModelSerializer):
    class Meta:
        model = Preposition
        fields = "__all__"

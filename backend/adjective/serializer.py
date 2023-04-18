from rest_framework.serializers import ModelSerializer
from .models import Adjective


class AdjectiveSerializer(ModelSerializer):
    class Meta:
        model = Adjective
        fields = "__all__"

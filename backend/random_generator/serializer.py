from rest_framework.serializers import ModelSerializer
from .models import RulesRandom

class RulesRandomSerializer(ModelSerializer):
    class Meta:
        model = RulesRandom
        fields = "__all__"
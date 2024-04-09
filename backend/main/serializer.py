from .models import Declentions, Gender, Time, Preposition, Tags, Infinitive
from rest_framework.serializers import ModelSerializer


class PrepositionSerializer(ModelSerializer):
    class Meta:
        model = Preposition
        fields = "__all__"


class TagsSerializer(ModelSerializer):
    class Meta:
        model = Tags
        fields = "__all__"


class DeclentionsSerializer(ModelSerializer):
    class Meta:
        model = Declentions
        fields = "__all__"


class GenderSerializer(ModelSerializer):
    class Meta:
        model = Gender
        fields = "__all__"


class TimeSerializer(ModelSerializer):
    class Meta:
        model = Time
        fields = "__all__"

class InfinitiveSerializer(ModelSerializer):
    class Meta:
        model = Infinitive
        fields = "__all__"

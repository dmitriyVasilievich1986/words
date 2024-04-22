from .models import Declentions, Gender, Time, Preposition, Tags, Infinitive, PartsOfSpeech
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

class InfinitiveSerializerDeep(ModelSerializer):
    class Meta:
        depth = 1
        model = Infinitive
        fields = (
            "part_of_speech",
            "translate",
            "word",
            "tags",
            "id",
        )

        read_only_fields = ("id", "part_of_speech")

class PartsOfSpeechSerializer(ModelSerializer):
    class Meta:
        model = PartsOfSpeech
        fields = "__all__"

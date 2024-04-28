from .models import Declentions, Gender, Time, Preposition, Tags, Infinitive, PartsOfSpeech, InfinitiveTags
from rest_framework.serializers import ModelSerializer
from verb.serializer import VerbSerializer


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

class PartsOfSpeechSerializer(ModelSerializer):
    class Meta:
        model = PartsOfSpeech
        fields = "__all__"

class InfinitiveTagsSerializer(ModelSerializer):
    class Meta:
        model = InfinitiveTags
        fields = "__all__"

class InfinitiveSerializer(ModelSerializer):
    class Meta:
        model = Infinitive
        fields = "__all__"

class InfinitiveSerializerDeep(ModelSerializer):
    tags = InfinitiveTagsSerializer(many=True, required=False, read_only=True)
    verb = VerbSerializer(many=True, required=False, read_only=True)
    
    class Meta:
        model = Infinitive
        fields = (
            "part_of_speech",
            "translate",
            "word",
            "tags",
            "verb",
            "id",
        )

        read_only_fields = ("id",)
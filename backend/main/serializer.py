from .models import Declentions, Gender, Time, Preposition, Tags, Infinitive, PartsOfSpeech, InfinitiveTags
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from pronoun.models import PersonalPronoun
from verb.serializer import VerbSerializer
from verb.models import Verb


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

class InfinitiveSerializer(ModelSerializer):
    class Meta:
        model = Infinitive
        fields = "__all__"

class InfinitiveSerializerDeep(ModelSerializer):
    verb = VerbSerializer(many=True, required=True)
    
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

        read_only_fields = ("id", "part_of_speech", "tags")

    def create(self, validated_data: dict) -> Infinitive:
        instance = super().create({k: v for k, v in validated_data.items() if k not in ("verb", "tags")})
        self._update_verbs(instance, validated_data.get("verb", None))
        self._update_tags(instance, validated_data.get("tags", None))
        return instance


    def update(self, instance: Infinitive, validated_data: dict) -> Infinitive:
        self._update_verbs(instance, validated_data.get("verb", None))
        self._update_tags(instance, validated_data.get("tags", None))
        return super().update(instance, {k: v for k, v in validated_data.items() if k not in ("verb", "tags")})

    def validate_verb(self, value: list[Verb]) -> list[Verb]:
        if value is None:
            return ValidationError("Field `verb` is required")
        elif PersonalPronoun.objects.all().count() != len(value):
            raise ValidationError("Verbs should contain all personal pronouns")
        return value

    def validate_tags(self, value: list[int]) -> list[Tags]:
        if value is None:
            return
        tags = Tags.objects.filter(id__in=value)
        if tags.count() != len(value):
            raise ValidationError("Some tags do not exist in the database")
        return tags

    def _update_verbs(self, instance: Infinitive, verbs: list[dict] = None) -> None:
        for verb in (verbs or list()):
            verb_instance: Verb = Verb.objects.get_or_create(**verb)[0]
            verb_instance.save()
            instance.verb.add(verb_instance)

    def _update_tags(self, instance: Infinitive, tags: list[Tags] = None) -> None:
        if tags is None:
            return
        InfinitiveTags.objects.filter(infinitive=instance).exclude(tags__in=tags).delete()
        infinitive_tags = [
            InfinitiveTags.objects.get_or_create(tags=t, infinitive=instance)[0]
            for t in tags
        ]
        instance.tags.set(infinitive_tags)
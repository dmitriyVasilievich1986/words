from rest_framework.serializers import ModelSerializer
from .models import Declentions, Gender, Time


# class NounInfinitiveSerializer(ModelSerializer):
#     noun = NounSerializer(many=True)

#     class Meta:
#         model = NounInfinitive
#         fields = "__all__"

#     def create(self, validated_data):
#         nouns = validated_data.pop("noun")
#         noun_infinitive = NounInfinitive.objects.create(**validated_data)
#         for noun in nouns:
#             Noun.objects.create(infinitive=noun_infinitive, **noun)
#         return noun_infinitive

#     def update(self, instance, validated_data):
#         nouns = validated_data.pop("noun")
#         NounInfinitive.objects.filter(id=instance.id).update(**validated_data)
#         for noun in nouns:
#             instance.noun.filter(
#                 declention=noun["declention"],
#                 gender=noun["gender"],
#                 plural=noun["plural"],
#             ).update(**noun)
#         return instance


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

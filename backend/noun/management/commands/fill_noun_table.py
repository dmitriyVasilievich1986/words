from django.core.management.base import BaseCommand
from main.models import Declentions, Gender
from ...models import Noun

cls = Noun
table = "noun"


class Command(BaseCommand):
    help = f"Fill {table} table with static values"

    def handle(self, *args, **kwargs):
        objects = [
            cls(
                declention=Declentions.objects.get(word="Nominative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="самолет",
                word="авион",
                base="авион",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Nominative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="самолеты",
                word="авиони",
                base="авион",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="самолету",
                word="авиону",
                base="авион",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="самолетам",
                word="авионима",
                base="авион",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Nominative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="тетрадь",
                word="свеска",
                base="свеск",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Nominative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="тетради",
                word="свеске",
                base="свеск",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="тетрадь",
                word="свески",
                base="свеск",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="тетради",
                word="свескама",
                base="свеск",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Nominative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="место",
                word="место",
                base="мест",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Nominative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="места",
                word="места",
                base="мест",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="месте",
                word="месту",
                base="мест",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="местах",
                word="местима",
                base="мест",
                plural=True,
            ),
        ]

        print(f"Clear {table} table")
        for obj in cls.objects.all():
            obj.delete()

        print(f"Filling {table} table:")
        for obj in objects:
            obj.save()
            print(f"\t{obj}")
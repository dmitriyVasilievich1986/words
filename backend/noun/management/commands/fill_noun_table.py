from django.core.management.base import BaseCommand
from main.models import Declentions, Gender
from ...models import Noun

cls = Noun
table = "noun"


class Command(BaseCommand):
    help = f"Fill {table} table with static values"

    def handle(self, *args, **kwargs):
        # region Nominative

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
        ]

        print(f"Clear {table} table")
        for obj in cls.objects.all():
            obj.delete()

        print(f"Filling {table} table:")
        for obj in objects:
            obj.save()
            print(f"\t{obj}")

        # endregion

        # region Dative

        objects = [
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="авион",
                word="авиону",
                base="авион",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="авиони",
                word="авионима",
                base="авион",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="свеска",
                word="свески",
                base="свеск",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="свеске",
                word="свескама",
                base="свеск",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="место",
                word="месту",
                base="мест",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="места",
                word="местима",
                base="мест",
                plural=True,
            ),
        ]

        for obj in objects:
            obj.save()
            print(f"\t{obj}")

        # endregion

        # region Locative

        objects = [
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="авион",
                word="авиону",
                base="авион",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="авиони",
                word="авионима",
                base="авион",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="свескa",
                word="свески",
                base="свеск",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="свескe",
                word="свескама",
                base="свеск",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="местo",
                word="месту",
                base="мест",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="места",
                word="местима",
                base="мест",
                plural=True,
            ),
        ]

        for obj in objects:
            obj.save()
            print(f"\t{obj}")

        # endregion

        # region Instrumental

        objects = [
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Masculine"),
                translate="авион",
                word="авионом",
                base="авион",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Masculine"),
                translate="авиони",
                word="авионима",
                base="авион",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Feminine"),
                translate="свеска",
                word="свеском",
                base="свеск",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Feminine"),
                translate="свеске",
                word="свескама",
                base="свеск",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Neuter"),
                translate="место",
                word="местом",
                base="мест",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Neuter"),
                translate="места",
                word="местима",
                base="мест",
                plural=True,
            ),
        ]

        for obj in objects:
            obj.save()
            print(f"\t{obj}")

        # endregion

        # region Accusative

        objects = [
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="авион",
                word="авион",
                base="авион",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="авиони",
                word="авионе",
                base="авион",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="свеска",
                word="свеску",
                base="свеск",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="свеске",
                word="свеске",
                base="свеск",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="место",
                word="место",
                base="мест",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="места",
                word="места",
                base="мест",
                plural=True,
            ),
        ]

        for obj in objects:
            obj.save()
            print(f"\t{obj}")

        # endregion

        # region Genitive

        objects = [
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Masculine"),
                translate="авион",
                word="авиона",
                base="авион",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Masculine"),
                translate="авиони",
                word="авиона",
                base="авион",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Feminine"),
                translate="свеска",
                word="свеске",
                base="свеск",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Feminine"),
                translate="свеске",
                word="свеске",
                base="свеск",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Neuter"),
                translate="место",
                word="места",
                base="мест",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Neuter"),
                translate="места",
                word="места",
                base="мест",
                plural=True,
            ),
        ]

        for obj in objects:
            obj.save()
            print(f"\t{obj}")

        # endregion

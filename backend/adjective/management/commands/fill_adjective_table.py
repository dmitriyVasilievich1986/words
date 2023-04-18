from django.core.management.base import BaseCommand
from main.models import Declentions, Gender
from ...models import Adjective

cls = Adjective
table = "adjective"


class Command(BaseCommand):
    help = f"Fill {table} table with static values"

    def handle(self, *args, **kwargs):
        objects = [
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="велик",
                word="великом",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="велика",
                word="великој",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="велико",
                word="великом",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="велики",
                word="великим",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="велике",
                word="великим",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="велика",
                word="великим",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="нов",
                word="новом",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="нова",
                word="новој",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="ново",
                word="новом",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="нови",
                word="новим",
                base="нов",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="нове",
                word="новим",
                base="нов",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Dative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="нова",
                word="новим",
                base="нов",
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

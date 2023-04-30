from django.core.management.base import BaseCommand
from main.models import Declentions, Gender
from ...models import Adjective

cls = Adjective
table = "adjective"


class Command(BaseCommand):
    help = f"Fill {table} table with static values"

    def handle(self, *args, **kwargs):
        # region Dative

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

        # endregion

        # region Locative

        objects = [
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="велик",
                word="великом",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="велика",
                word="великој",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="велико",
                word="великом",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="велики",
                word="великим",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="велике",
                word="великим",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="велика",
                word="великим",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="нов",
                word="новом",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="нова",
                word="новој",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="ново",
                word="новом",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="нови",
                word="новим",
                base="нов",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="нове",
                word="новим",
                base="нов",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Locative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="нова",
                word="новим",
                base="нов",
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
                translate="велик",
                word="великим",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Feminine"),
                translate="велика",
                word="великом",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Neuter"),
                translate="велико",
                word="великим",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Masculine"),
                translate="велики",
                word="великим",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Feminine"),
                translate="велике",
                word="великим",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Neuter"),
                translate="велика",
                word="великим",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Masculine"),
                translate="нов",
                word="новим",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Feminine"),
                translate="нова",
                word="новом",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Neuter"),
                translate="ново",
                word="новим",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Masculine"),
                translate="нови",
                word="новим",
                base="нов",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Feminine"),
                translate="нове",
                word="новим",
                base="нов",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Instrumental"),
                gender=Gender.objects.get(word="Neuter"),
                translate="нова",
                word="новим",
                base="нов",
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
                translate="велики",
                word="велики",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="велика",
                word="велику",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="велико",
                word="велико",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="велики",
                word="велике",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="велике",
                word="велике",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="велика",
                word="велика",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="нови",
                word="нови",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="нову",
                word="нову",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="ново",
                word="ново",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Masculine"),
                translate="нови",
                word="нове",
                base="нов",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Feminine"),
                translate="нове",
                word="нове",
                base="нов",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Accusative"),
                gender=Gender.objects.get(word="Neuter"),
                translate="нова",
                word="нова",
                base="нов",
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
                translate="велики",
                word="великог",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Feminine"),
                translate="велика",
                word="велике",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Neuter"),
                translate="велико",
                word="великог",
                base="велик",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Masculine"),
                translate="велики",
                word="великих",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Feminine"),
                translate="велике",
                word="великих",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Neuter"),
                translate="велика",
                word="великих",
                base="велик",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Masculine"),
                translate="нови",
                word="новог",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Feminine"),
                translate="нову",
                word="нове",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Neuter"),
                translate="ново",
                word="новог",
                base="нов",
                plural=False,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Masculine"),
                translate="нови",
                word="нових",
                base="нов",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Feminine"),
                translate="нове",
                word="нових",
                base="нов",
                plural=True,
            ),
            cls(
                declention=Declentions.objects.get(word="Genitive"),
                gender=Gender.objects.get(word="Neuter"),
                translate="нова",
                word="нових",
                base="нов",
                plural=True,
            ),
        ]

        for obj in objects:
            obj.save()
            print(f"\t{obj}")

        # endregion

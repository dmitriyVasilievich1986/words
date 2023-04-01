from django.core.management.base import BaseCommand
from main.models import Declentions
from ...models import Pronoun

cls = Pronoun
table = "pronoun"


class Command(BaseCommand):
    help = f"Fill {table} table with static values"

    def handle(self, *args, **kwargs):
        declention = Declentions.objects.get(word="Nominative")
        objects = [
            cls(declention=declention, translate="я", word="ја"),
            cls(declention=declention, translate="ты", word="ти"),
            cls(declention=declention, translate="он", word="он"),
            cls(declention=declention, translate="вы", plural=True, word="ви"),
            cls(declention=declention, translate="мы", plural=True, word="ми"),
            cls(declention=declention, translate="они", plural=True, word="они"),
        ]

        print(f"Clear {table} table")
        for obj in cls.objects.all():
            obj.delete()

        print(f"Filling {table} table:")
        for obj in objects:
            obj.save()
            print(f"\t{obj}")

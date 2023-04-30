from django.core.management.base import BaseCommand
from main.models import Declentions

cls = Declentions
table = "declentions"


class Command(BaseCommand):
    help = f"Fill {table} table with static values"

    def handle(self, *args, **kwargs):
        objects = [
            cls(word="Instrumental", translate="Инструментальный"),
            cls(word="Nominative", translate="Именительный"),
            cls(word="Accusative", translate="Винительный"),
            cls(word="Genitive", translate="Родительный"),
            cls(word="Locative", translate="Местный"),
            cls(word="Dative", translate="Дательный"),
        ]

        print(f"Clear {table} table")
        for obj in cls.objects.all():
            obj.delete()

        print(f"Filling {table} table:")
        for obj in objects:
            obj.save()
            print(f"\t{obj}")

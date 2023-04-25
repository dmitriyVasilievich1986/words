from django.core.management.base import BaseCommand
from main.models import Tags

cls = Tags
table = "tags"


class Command(BaseCommand):
    help = f"Fill {table} table with static values"

    def handle(self, *args, **kwargs):
        objects = [
            cls(word="instrumental"),
            cls(word="locative"),
            cls(word="dative"),
        ]

        print(f"Clear {table} table")
        for obj in cls.objects.all():
            obj.delete()

        print(f"Filling {table} table:")
        for obj in objects:
            obj.save()
            print(f"\t{obj}")

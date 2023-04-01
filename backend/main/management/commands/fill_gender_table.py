from django.core.management.base import BaseCommand
from main.models import Gender

cls = Gender
table = "gender"


class Command(BaseCommand):
    help = f"Fill {table} table with static values"

    def handle(self, *args, **kwargs):
        objects = [
            cls(word="Masculine", translate="Мужской"),
            cls(word="Feminine", translate="Женский"),
            cls(word="Neuter", translate="Средний"),
        ]

        print(f"Clear {table} table")
        for obj in cls.objects.all():
            obj.delete()

        print(f"Filling {table} table:")
        for obj in objects:
            obj.save()
            print(f"\t{obj}")

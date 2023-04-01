from django.core.management.base import BaseCommand
from main.models import Time

cls = Time
table = "time"


class Command(BaseCommand):
    help = f"Fill {table} table with static values"

    def handle(self, *args, **kwargs):
        objects = [
            cls(word="Present", translate="Настоящее"),
            cls(word="Future", translate="Будущее"),
            cls(word="Past", translate="Прошлое"),
        ]

        print(f"Clear {table} table")
        for obj in cls.objects.all():
            obj.delete()

        print(f"Filling {table} table:")
        for obj in objects:
            obj.save()
            print(f"\t{obj}")

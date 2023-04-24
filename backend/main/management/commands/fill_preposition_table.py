from django.core.management.base import BaseCommand
from ...models import Preposition

cls = Preposition
table = "preposition"


class Command(BaseCommand):
    help = f"Fill {table} table with static values"

    def handle(self, *args, **kwargs):
        objects = [
            cls(translate="на", word="на"),
            cls(translate="в", word="у"),
            cls(translate="к", word="к"),
            cls(translate="ка", word="ка"),
            cls(translate="према", word="према"),
            cls(translate="по", word="по"),
            cls(translate="с", word="о"),
            cls(translate="при", word="при"),
            cls(translate="са", word="са"),
            cls(translate="над", word="над"),
            cls(translate="под", word="под"),
            cls(translate="перед", word="пред"),
            cls(translate="от", word="од"),
            cls(translate="до", word="до"),
            cls(translate="из", word="из"),
            cls(translate="перед", word="испред"),
        ]

        print(f"Clear {table} table")
        for obj in cls.objects.all():
            obj.delete()

        print(f"Filling {table} table:")
        for obj in objects:
            obj.save()
            print(f"\t{obj}")

from django.core.management.base import BaseCommand
from ...models import Preposition

cls = Preposition
table = "preposition"


class Command(BaseCommand):
    help = f"Fill {table} table with static values"

    def handle(self, *args, **kwargs):
        objects = [
            cls(translate="на", word="на"),
            cls(translate="у", word="у"),
            cls(translate="к", word="к"),
            cls(translate="ка", word="ка"),
            cls(translate="према", word="према"),
            cls(translate="по", word="по"),
            cls(translate="о", word="о"),
            cls(translate="при", word="при"),
            cls(translate="са", word="са"),
            cls(translate="над", word="над"),
            cls(translate="под", word="под"),
            cls(translate="пред", word="пред"),
            cls(translate="од", word="од"),
            cls(translate="до", word="до"),
            cls(translate="из", word="из"),
            cls(translate="испред", word="испред"),
            cls(translate="близу", word="близу"),
            cls(translate="испод", word="испод"),
            cls(translate="изнад", word="изнад"),
        ]

        print(f"Clear {table} table")
        for obj in cls.objects.all():
            obj.delete()

        print(f"Filling {table} table:")
        for obj in objects:
            obj.save()
            print(f"\t{obj}")

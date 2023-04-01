from django.core.management.base import BaseCommand
from pronoun.models import Pronoun
from main.models import Time
from ...models import Verb

cls = Verb
table = "verb"


class Command(BaseCommand):
    help = f"Fill {table} table with static values"

    def handle(self, *args, **kwargs):
        objects = [
            cls(
                pronoun=Pronoun.objects.get(word="ја"),
                time=Time.objects.get(word="Past"),
                translate="был",
                word="сам",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ти"),
                time=Time.objects.get(word="Past"),
                translate="был",
                word="си",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="он"),
                time=Time.objects.get(word="Past"),
                translate="был",
                word="је",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ви"),
                time=Time.objects.get(word="Past"),
                translate="были",
                word="сте",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ми"),
                time=Time.objects.get(word="Past"),
                translate="были",
                word="смо",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="они"),
                time=Time.objects.get(word="Past"),
                translate="были",
                word="су",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ја"),
                time=Time.objects.get(word="Future"),
                translate="буду",
                word="ћу",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ти"),
                time=Time.objects.get(word="Future"),
                translate="будешь",
                word="ћеш",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="он"),
                time=Time.objects.get(word="Future"),
                translate="будет",
                word="ће",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ви"),
                time=Time.objects.get(word="Future"),
                translate="будете",
                word="ћете",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ми"),
                time=Time.objects.get(word="Future"),
                translate="будем",
                word="ћемо",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="они"),
                time=Time.objects.get(word="Future"),
                translate="будут",
                word="ће",
            ),
            cls(
                translate="любить",
                word="волети",
                base="вол",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ја"),
                time=Time.objects.get(word="Present"),
                translate="люблю",
                word="волим",
                base="вол",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ти"),
                time=Time.objects.get(word="Present"),
                translate="любишь",
                word="волиш",
                base="вол",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="он"),
                time=Time.objects.get(word="Present"),
                translate="любит",
                word="воли",
                base="вол",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ви"),
                time=Time.objects.get(word="Present"),
                translate="любите",
                word="волите",
                base="вол",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ми"),
                time=Time.objects.get(word="Present"),
                translate="любим",
                word="волимо",
                base="вол",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="они"),
                time=Time.objects.get(word="Present"),
                translate="любят",
                word="воле",
                base="вол",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ја"),
                time=Time.objects.get(word="Past"),
                translate="любил",
                word="волео",
                base="вол",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ја"),
                time=Time.objects.get(word="Future"),
                translate="любить",
                word="волети",
                base="вол",
            ),
        ]

        print(f"Clear {table} table")
        for obj in cls.objects.all():
            obj.delete()

        print(f"Filling {table} table:")
        for obj in objects:
            obj.save()
            print(f"\t{obj}")

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
                word="сам",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ти"),
                time=Time.objects.get(word="Past"),
                word="си",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="он"),
                time=Time.objects.get(word="Past"),
                word="је",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ви"),
                time=Time.objects.get(word="Past"),
                word="сте",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ми"),
                time=Time.objects.get(word="Past"),
                word="смо",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="они"),
                time=Time.objects.get(word="Past"),
                word="су",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ја"),
                time=Time.objects.get(word="Future"),
                word="ћу",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ти"),
                time=Time.objects.get(word="Future"),
                word="ћеш",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="он"),
                time=Time.objects.get(word="Future"),
                word="ће",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ви"),
                time=Time.objects.get(word="Future"),
                word="ћете",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ми"),
                time=Time.objects.get(word="Future"),
                word="ћемо",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="они"),
                time=Time.objects.get(word="Future"),
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
                time=Time.objects.get(word="Past"),
                translate="волети",
                word="волео",
                base="вол",
            ),
            cls(
                time=Time.objects.get(word="Future"),
                translate="волети",
                word="волети",
                base="вол",
            ),
            cls(
                translate="видеть",
                word="видети",
                base="вид",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ја"),
                time=Time.objects.get(word="Present"),
                translate="вижу",
                word="волим",
                base="вид",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ти"),
                time=Time.objects.get(word="Present"),
                translate="видишь",
                word="видиш",
                base="вид",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="он"),
                time=Time.objects.get(word="Present"),
                translate="видит",
                word="види",
                base="вид",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ви"),
                time=Time.objects.get(word="Present"),
                translate="видите",
                word="видите",
                base="вид",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="ми"),
                time=Time.objects.get(word="Present"),
                translate="видим",
                word="видимо",
                base="вид",
            ),
            cls(
                pronoun=Pronoun.objects.get(word="они"),
                time=Time.objects.get(word="Present"),
                translate="видят",
                word="виде",
                base="вид",
            ),
            cls(
                time=Time.objects.get(word="Past"),
                translate="видети",
                word="видео",
                base="вид",
            ),
            cls(
                time=Time.objects.get(word="Future"),
                translate="видети",
                word="видети",
                base="вид",
            ),
        ]

        print(f"Clear {table} table")
        for obj in cls.objects.all():
            obj.delete()

        print(f"Filling {table} table:")
        for obj in objects:
            obj.save()
            print(f"\t{obj}")

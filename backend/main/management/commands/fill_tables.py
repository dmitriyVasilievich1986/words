from django.core.management.base import BaseCommand
from django.core import management


class Command(BaseCommand):
    help = f"Fill all tables with static values"

    def handle(self, *args, **kwargs):
        print("***Declentions***")
        management.call_command("fill_declentions_table")
        print("***Pronoun***")
        management.call_command("fill_pronoun_table")
        print("***Gender***")
        management.call_command("fill_gender_table")
        print("***Time***")
        management.call_command("fill_time_table")
        print("***Verb***")
        management.call_command("fill_verb_table")
        print("***Noun***")
        management.call_command("fill_noun_table")

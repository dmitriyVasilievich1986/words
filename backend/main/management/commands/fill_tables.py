from django.core.management.base import BaseCommand
from django.core import management


class Command(BaseCommand):
    help = f"Fill all tables with static values"

    def handle(self, *args, **kwargs):
        print("***Prepositions***")
        management.call_command("fill_preposition_table")
        print("***Declentions***")
        management.call_command("fill_declentions_table")
        print("***Pronoun***")
        management.call_command("fill_pronoun_table")
        print("***Gender***")
        management.call_command("fill_gender_table")
        print("***Time***")
        management.call_command("fill_time_table")
        print("***Tags***")
        management.call_command("fill_tags_table")

        print("***Adjective***")
        management.call_command("fill_adjective_table")
        print("***Verb***")
        management.call_command("fill_verb_table")
        print("***Noun***")
        management.call_command("fill_noun_table")

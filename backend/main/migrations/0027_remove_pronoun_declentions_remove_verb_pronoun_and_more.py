# Generated by Django 4.1.2 on 2023-04-01 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0026_remove_noun_infinitive_noun_base_noun_gender_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pronoun",
            name="declentions",
        ),
        migrations.RemoveField(
            model_name="verb",
            name="pronoun",
        ),
        migrations.RemoveField(
            model_name="verb",
            name="time",
        ),
        migrations.DeleteModel(
            name="Noun",
        ),
        migrations.DeleteModel(
            name="Pronoun",
        ),
        migrations.DeleteModel(
            name="Verb",
        ),
    ]

# Generated by Django 4.2.11 on 2024-04-10 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0035_infinitive_part_of_speech"),
        ("verb", "0004_remove_verb_base_remove_verb_preposition_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="verb",
            name="infinitive",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="verb",
                to="main.infinitive",
            ),
        ),
    ]
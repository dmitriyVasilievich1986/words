# Generated by Django 4.1.2 on 2023-04-01 07:32

from django.db import migrations, models
import django.db.models.deletion
import main.support_mixin


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main", "0027_remove_pronoun_declentions_remove_verb_pronoun_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Pronoun",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("translate", models.CharField(max_length=50)),
                ("word", models.CharField(max_length=50)),
                ("plural", models.BooleanField(default=False)),
                (
                    "declentions",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pronoun",
                        to="main.declentions",
                    ),
                ),
            ],
            bases=(
                main.support_mixin.RepresentationClass,
                models.Model,
                main.support_mixin.RandomMixin,
            ),
        ),
    ]

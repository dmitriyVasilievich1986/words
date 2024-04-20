# Generated by Django 4.2.11 on 2024-04-10 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0032_infinitive"),
    ]

    operations = [
        migrations.CreateModel(
            name="PartsOfSpeech",
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
                ("translate", models.CharField(max_length=150)),
                ("word", models.CharField(max_length=150)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]

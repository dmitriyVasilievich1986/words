# Generated by Django 4.1.2 on 2023-02-25 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0017_time_remove_verb_declention_verb_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="verb",
            name="plural",
        ),
    ]

# Generated by Django 4.1.2 on 2023-02-18 12:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0014_verbinfinitive_base"),
    ]

    operations = [
        migrations.RenameField(
            model_name="noun",
            old_name="noun",
            new_name="infinitive",
        ),
    ]
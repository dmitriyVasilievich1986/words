# Generated by Django 4.1.2 on 2023-04-12 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("preposition", "0001_initial"),
        ("noun", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="noun",
            name="preposition",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="noun",
                to="preposition.preposition",
            ),
        ),
    ]
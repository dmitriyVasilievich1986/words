# Generated by Django 4.2.11 on 2024-04-28 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0040_auto_20240428_1310"),
        ("verb", "0012_auto_20240428_1321"),
    ]

    operations = [
        migrations.AlterField(
            model_name="verb",
            name="time",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="verb",
                to="main.time",
            ),
        ),
    ]

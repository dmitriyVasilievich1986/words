# Generated by Django 4.1.2 on 2022-10-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="verb",
            name="translate",
            field=models.CharField(default="a", max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="verbdeclension",
            name="translate",
            field=models.CharField(default="a", max_length=150),
            preserve_default=False,
        ),
    ]
# Generated by Django 4.2.11 on 2024-04-09 18:00

from django.db import migrations

def insert_pp(apps, schema_editor):
    PersonalPronoun = apps.get_model('pronoun', 'PersonalPronoun')
    pps = (
        ("ja", "я"),
        ("ти", "ты"),
        ("он", "он"),
        ("она", "она"),
        ("оно", "оно"),
        ("ми", "мы"),
        ("ви", "вы"),
        ("они", "они"),
        ("они", "оне"),
        ("они", "она"),
    )
    for word, translate in pps:
        pp = PersonalPronoun.objects.create(word=word, translate=translate)
        pp.save()

def remove_pp(apps, schema_editor):
    PersonalPronoun = apps.get_model('pronoun', 'PersonalPronoun')
    PersonalPronoun.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("pronoun", "0003_personalpronoun"),
    ]

    operations = [
        migrations.RunPython(insert_pp, remove_pp),
    ]

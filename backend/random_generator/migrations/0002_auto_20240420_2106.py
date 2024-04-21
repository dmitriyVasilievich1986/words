# Generated by Django 4.2.11 on 2024-04-20 21:06

from django.db import migrations

def set_default_rules_random(apps, schema_editor):
    RulesRandom = apps.get_model('random_generator', 'RulesRandom')

    RulesRandom.objects.create(
        description="Переведите глагол в форме номинатива",
        name="Глагол",
    ).save()

    RulesRandom.objects.create(
        description="Просклоняйте глагол по формуле: [Личное местоимение] [Глагол]",
        name="Склонение глагола",
    ).save()

def remove_rules_random(apps, schema_editor):
    RulesRandom = apps.get_model('random_generator', 'RulesRandom')
    RulesRandom.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ("random_generator", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(set_default_rules_random, remove_rules_random),
    ]
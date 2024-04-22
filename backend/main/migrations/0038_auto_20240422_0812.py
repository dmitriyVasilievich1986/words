# Generated by Django 4.2.11 on 2024-04-22 08:12

from django.db import migrations

def insert_tags(apps, schema_editor):
    Tags = apps.get_model('main', 'Tags')
    Tags.objects.create(
        word="глагол -им",
        hidden=False,
    ).save()
    Tags.objects.create(
        word="глагол -ам",
        hidden=False,
    ).save()
    Tags.objects.create(
        word="глагол -ем",
        hidden=False,
    ).save()
    Tags.objects.create(
        word="движение",
        hidden=False,
    ).save()

def remove_tags(apps, schema_editor):
    Tags = apps.get_model('main', 'Tags')
    Tags.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0037_alter_infinitive_part_of_speech"),
    ]

    operations = [
        migrations.RunPython(insert_tags, remove_tags),
    ]
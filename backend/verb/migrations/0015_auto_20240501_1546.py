# Generated by Django 4.2.11 on 2024-05-01 15:46

from django.db import migrations

def insert_time_verb(apps, schema_editor):
    TimeVerb = apps.get_model('verb', 'TimePersonalPronounVerb')
    PersonalPronoun = apps.get_model('pronoun', 'PersonalPronoun')
    Time = apps.get_model('main', 'Time')

    future_time = Time.objects.get(word="Future")
    past_time = Time.objects.get(word="Past")

    TimeVerb(
        word="ћу",
        time=future_time,
        personal_pronoun=PersonalPronoun.objects.get(word="ja"),
    ).save()
    TimeVerb(
        word="ћеш",
        time=future_time,
        personal_pronoun=PersonalPronoun.objects.get(word="ти"),
    ).save()
    TimeVerb(
        word="ћете",
        time=future_time,
        personal_pronoun=PersonalPronoun.objects.get(word="ви"),
    ).save()
    TimeVerb(
        word="ћемо",
        time=future_time,
        personal_pronoun=PersonalPronoun.objects.get(word="ми"),
    ).save()
    for pp in PersonalPronoun.objects.filter(translate__in=["они", "он", "она", "оно"]):
        TimeVerb(
            word="ће",
            time=future_time,
            personal_pronoun=pp,
        ).save()
    
    TimeVerb(
        word="сам",
        time=past_time,
        personal_pronoun=PersonalPronoun.objects.get(word="ja"),
    ).save()
    TimeVerb(
        word="си",
        time=past_time,
        personal_pronoun=PersonalPronoun.objects.get(word="ти"),
    ).save()
    TimeVerb(
        word="сте",
        time=past_time,
        personal_pronoun=PersonalPronoun.objects.get(word="ви"),
    ).save()
    TimeVerb(
        word="смо",
        time=past_time,
        personal_pronoun=PersonalPronoun.objects.get(word="ми"),
    ).save()
    for pp in PersonalPronoun.objects.filter(translate__in=["они", "он", "она", "оно"]):
        TimeVerb(
            word="ће",
            time=past_time,
            personal_pronoun=pp,
        ).save()



def remove_time_verb(apps, schema_editor):
    TimeVerb = apps.get_model('verb', 'TimePersonalPronounVerb')
    TimeVerb.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ("verb", "0014_timepersonalpronounverb"),
    ]

    operations = [
        migrations.RunPython(insert_time_verb, remove_time_verb),
    ]
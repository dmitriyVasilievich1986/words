# Generated by Django 4.1.2 on 2023-03-31 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0022_remove_pronoun_declentions_remove_pronoun_gender_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="verb",
            name="infinitive",
        ),
        migrations.AddField(
            model_name="verb",
            name="base",
            field=models.CharField(default=None, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="verb",
            name="pronoun",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="verb",
                to="main.pronoun",
            ),
        ),
        migrations.DeleteModel(
            name="VerbInfinitive",
        ),
    ]
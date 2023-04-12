# Generated by Django 4.1.2 on 2023-03-03 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0020_pronoun_declentions"),
    ]

    operations = [
        migrations.AddField(
            model_name="pronoun",
            name="personal_pronoun",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pronoun",
                to="main.personalpronoun",
            ),
        ),
    ]
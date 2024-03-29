# Generated by Django 4.1.2 on 2023-03-31 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0024_pronoun_been_pronoun_personal"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pronoun",
            name="been",
        ),
        migrations.RemoveField(
            model_name="pronoun",
            name="personal",
        ),
        migrations.AddField(
            model_name="pronoun",
            name="declentions",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="pronoun",
                to="main.declentions",
            ),
        ),
        migrations.AddField(
            model_name="pronoun",
            name="plural",
            field=models.BooleanField(default=False),
        ),
    ]

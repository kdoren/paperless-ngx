# Generated by Django 5.1.1 on 2024-09-30 15:17

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        (
            "paperless_mail",
            "0025_alter_mailaccount_owner_alter_mailrule_owner_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="mailrule",
            name="enabled",
            field=models.BooleanField(default=True, verbose_name="enabled"),
        ),
    ]
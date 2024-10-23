# Generated by Django 5.1.1 on 2024-10-24 04:03

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [
        ("documents", "1055_alter_storagepath_path"),
    ]

    operations = [
        migrations.AddField(
            model_name="workflowtrigger",
            name="schedule_delay",
            field=models.CharField(
                blank=True,
                help_text="The delay before the scheduled trigger is activated.",
                max_length=256,
                null=True,
                verbose_name="schedule delay",
            ),
        ),
        migrations.AddField(
            model_name="workflowtrigger",
            name="schedule_delay_custom_field",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="documents.customfield",
                verbose_name="schedule delay custom field",
            ),
        ),
        migrations.AddField(
            model_name="workflowtrigger",
            name="schedule_delay_field",
            field=models.CharField(
                choices=[
                    ("added", "Added"),
                    ("created", "Created"),
                    ("modified", "Modified"),
                    ("custom_field", "Custom Field"),
                ],
                default="added",
                help_text="The field to use for the delay.",
                max_length=20,
                verbose_name="schedule delay field",
            ),
        ),
        migrations.AddField(
            model_name="workflowtrigger",
            name="schedule_is_recurring",
            field=models.BooleanField(
                default=False,
                help_text="If the schedule should be recurring.",
                verbose_name="schedule is recurring",
            ),
        ),
        migrations.AlterField(
            model_name="workflowtrigger",
            name="type",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "Consumption Started"),
                    (2, "Document Added"),
                    (3, "Document Updated"),
                    (4, "Scheduled"),
                ],
                default=1,
                verbose_name="Workflow Trigger Type",
            ),
        ),
        migrations.CreateModel(
            name="WorkflowRun",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "run_at",
                    models.DateTimeField(
                        db_index=True,
                        default=django.utils.timezone.now,
                        verbose_name="date run",
                    ),
                ),
                (
                    "document",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="workflow_runs",
                        to="documents.document",
                        verbose_name="document",
                    ),
                ),
                (
                    "workflow",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="runs",
                        to="documents.workflow",
                        verbose_name="workflow",
                    ),
                ),
            ],
            options={
                "verbose_name": "workflow run",
                "verbose_name_plural": "workflow runs",
            },
        ),
    ]

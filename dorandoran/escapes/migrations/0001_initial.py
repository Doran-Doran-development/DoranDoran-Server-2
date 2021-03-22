# Generated by Django 3.1.7 on 2021-03-17 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="EscapeQueue",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="id", primary_key=True, serialize=False),
                ),
                (
                    "reason",
                    models.CharField(
                        default="reason", max_length=100, verbose_name="reason"
                    ),
                ),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "accepted"),
                            (2, "denied"),
                            (3, "waiting"),
                            (4, "expired"),
                        ],
                        default=3,
                    ),
                ),
                ("start_at", models.DateTimeField(verbose_name="start time")),
                ("end_at", models.DateTimeField(verbose_name="end time")),
                (
                    "applicant_id",
                    models.ForeignKey(
                        db_column="applicant_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.user",
                    ),
                ),
            ],
            options={
                "db_table": "EscapeQueue",
            },
        ),
    ]

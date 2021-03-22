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
            name="Team",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="id", primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=25)),
                ("description", models.CharField(max_length=250, null=True)),
                (
                    "applicant_id",
                    models.ForeignKey(
                        db_column="applicant_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="TeamMember",
            fields=[
                (
                    "id",
                    models.AutoField(db_column="id", primary_key=True, serialize=False),
                ),
                (
                    "member_id",
                    models.ForeignKey(
                        db_column="member_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.user",
                    ),
                ),
                (
                    "team_id",
                    models.ForeignKey(
                        db_column="team_id",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="teams.team",
                    ),
                ),
            ],
            options={
                "unique_together": {("team_id", "member_id")},
            },
        ),
    ]

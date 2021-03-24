# Generated by Django 3.1.7 on 2021-03-22 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_profile_user_primary_key"),
    ]

    operations = [
        migrations.CreateModel(
            name="TeacherCertificationCode",
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
                ("certification_code", models.CharField(max_length=20)),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]

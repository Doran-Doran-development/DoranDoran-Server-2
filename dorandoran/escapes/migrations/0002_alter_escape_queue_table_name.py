# Generated by Django 3.1.7 on 2021-03-19 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("escapes", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelTable(
            name="escapequeue",
            table="escape_queue",
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-16 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='id',
            field=models.PositiveSmallIntegerField(choices=[(3, 'admin'), (1, 'student'), (2, 'teacher')], primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-22 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_alter_habit_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='periodicity',
            field=models.CharField(max_length=10),
        ),
    ]

# Generated by Django 4.2.2 on 2023-06-23 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0005_completedhabit'),
    ]

    operations = [
        migrations.AddField(
            model_name='habit',
            name='streak',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='habit',
            name='streak_type',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]

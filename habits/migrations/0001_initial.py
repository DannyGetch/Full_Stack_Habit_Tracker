# Generated by Django 4.2.2 on 2023-06-22 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('periodicity', models.CharField(max_length=20)),
                ('duration', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 4.0.4 on 2023-01-03 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Recommender', '0006_movie_watched'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='watched',
        ),
    ]

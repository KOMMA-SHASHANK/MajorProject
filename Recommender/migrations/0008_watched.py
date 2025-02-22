# Generated by Django 4.0.4 on 2023-01-03 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recommender', '0007_remove_movie_watched'),
    ]

    operations = [
        migrations.CreateModel(
            name='Watched',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField(default=False)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recommender.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recommender.newuser')),
            ],
        ),
    ]

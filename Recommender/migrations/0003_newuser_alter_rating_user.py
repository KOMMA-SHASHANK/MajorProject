# Generated by Django 4.0.4 on 2023-01-01 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Recommender', '0002_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='newUser',
            fields=[
                ('userId', models.IntegerField(primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recommender.newuser'),
        ),
    ]

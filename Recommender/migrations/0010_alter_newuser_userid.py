# Generated by Django 4.0.4 on 2023-01-07 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recommender', '0009_alter_newuser_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='userId',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 3.0.8 on 2023-04-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_regform_movies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regform',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]

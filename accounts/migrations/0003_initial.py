# Generated by Django 4.0.4 on 2023-01-09 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Recommender', '0012_delete_regform'),
        ('accounts', '0002_delete_regform'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('genres', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recommender.newuser')),
            ],
        ),
    ]

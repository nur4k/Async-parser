# Generated by Django 4.2.5 on 2023-09-20 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_apartment', models.CharField(max_length=155, verbose_name='id')),
                ('value', models.CharField(max_length=155, verbose_name='Значение')),
                ('latitude', models.CharField(max_length=155, verbose_name='Широта')),
                ('longtitude', models.CharField(max_length=155, verbose_name='Долгота')),
            ],
        ),
    ]

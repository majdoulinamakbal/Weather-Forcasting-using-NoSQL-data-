# Generated by Django 2.2.12 on 2020-06-22 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Casablanca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.FloatField()),
                ('temperature', models.FloatField()),
                ('humidite', models.IntegerField()),
                ('vent', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]

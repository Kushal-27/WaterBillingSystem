# Generated by Django 4.0.4 on 2022-05-04 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rates'),
    ]

    operations = [
        migrations.AddField(
            model_name='rates',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]

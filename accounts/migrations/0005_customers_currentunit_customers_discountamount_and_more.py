# Generated by Django 4.0.4 on 2022-05-03 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_users_citizenship'),
    ]

    operations = [
        migrations.AddField(
            model_name='customers',
            name='currentunit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customers',
            name='discountamount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customers',
            name='fineamount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customers',
            name='meterno',
            field=models.CharField(default=None, max_length=200, unique=True),
        ),
        migrations.AddField(
            model_name='customers',
            name='previousunit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='customers',
            name='totaldue',
            field=models.IntegerField(default=0),
        ),
    ]

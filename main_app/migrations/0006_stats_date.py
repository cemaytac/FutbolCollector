# Generated by Django 3.1.1 on 2020-10-08 14:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_auto_20201008_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='stats',
            name='date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date Recorded'),
        ),
    ]

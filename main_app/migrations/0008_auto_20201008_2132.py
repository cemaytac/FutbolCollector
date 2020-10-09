# Generated by Django 3.1.1 on 2020-10-08 21:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20201008_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_type', models.CharField(max_length=50, verbose_name='Training Type')),
                ('date', models.DateField(default=datetime.date.today)),
                ('duration', models.IntegerField()),
                ('completed', models.BooleanField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='stats',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='player',
            name='training',
            field=models.ManyToManyField(to='main_app.Training'),
        ),
    ]
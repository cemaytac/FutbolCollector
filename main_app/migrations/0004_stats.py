# Generated by Django 3.1.1 on 2020-10-08 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20201006_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appearances', models.IntegerField()),
                ('goals', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('clean_sheets', models.IntegerField()),
                ('shots', models.IntegerField()),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.player')),
            ],
        ),
    ]

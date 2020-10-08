from django.db import models
from django.urls import reverse
from datetime import date


class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    kitNumber = models.IntegerField('Kit Number')
    position = models.CharField(max_length=3)
    preferredFoot = models.CharField('Preferred Foot', max_length=5)
    appearances = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['kitNumber']

    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})


class Stats(models.Model):
    appearances = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()
    clean_sheets = models.IntegerField()
    shots = models.IntegerField()
    date = models.DateField("Date Recorded", default=date.today)

    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"Player scored {self.goals} in {self.appearances} games"

# class Equipment(models.Model):
#     cleats = models.BooleanField()
#     cleats_brand = models.CharField(max_length=50)
#     jersey_home = models.BooleanField()
#     jersey_away = models.BooleanField()
#     shorts = models.BooleanField()
#     socks = models.BooleanField()
#     shin_guards = models.BooleanField()

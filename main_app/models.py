from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

POSITIONS = [
    ('GK', 'Goalkeeper'),
    ('DEF', 'Defender'),
    ('MID', 'Midfielder'),
    ('FW', 'Forward'),
]

PREFERRED_FOOT = [
    ('R', 'Right'),
    ('L', 'Left'),
    ('B', 'Both'),
]

# call this


class Training(models.Model):
    training_type = models.CharField("Training Type", max_length=50)
    date = models.DateField(default=date.today)
    duration = models.IntegerField()
    completed = models.BooleanField()

    def __str__(self):
        return f"{self.training_type}, {self.date}"

    def get_absolute_url(self):
        return reverse('trainings_detail', kwargs={'pk': self.id})


class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    kitNumber = models.IntegerField('Kit Number')
    position = models.CharField(
        max_length=3, choices=POSITIONS, default=POSITIONS[0][0])
    preferredFoot = models.CharField(
        'Preferred Foot', max_length=1, choices=PREFERRED_FOOT, default=PREFERRED_FOOT[0][0])
    trainings = models.ManyToManyField(Training)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.get_position_display()}"

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

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.player.name} scored {self.goals} in {self.appearances} games"


# class Equipment(models.Model):
#     cleats = models.BooleanField()
#     cleats_brand = models.CharField(max_length=50)
#     jersey_home = models.BooleanField()
#     jersey_away = models.BooleanField()
#     shorts = models.BooleanField()
#     socks = models.BooleanField()
#     shin_guards = models.BooleanField()

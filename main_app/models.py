from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    kitNumber = models.IntegerField()
    position = models.CharField(max_length=3)
    preferredFoot = models.CharField(max_length=5)
    appearances = models.IntegerField()
    goals = models.IntegerField()
    assists = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['kitNumber']

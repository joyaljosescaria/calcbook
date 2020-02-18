from django.db import models
from django.utils import timezone

class Tab(models.Model):
    date = models.DateField(default=timezone.now , unique=True)
    bank = models.FloatField()
    janasevana = models.FloatField()
    borrow = models.FloatField()
    internet = models.FloatField()
    utilities = models.FloatField()
    recharge = models.FloatField()
    inhand = models.FloatField()
    total = models.FloatField()
    def __str__(self):
        return str(self.date)

class Borrow(models.Model):
    name = models.CharField(max_length=100)
    rented = models.IntegerField()
    def __str__(self):
        return self.name

class Balance(models.Model):
    date = models.DateField(default=timezone.now)
    balance = models.FloatField()
    diff = models.FloatField()
    def __str__(self):
        return str(self.date)

from django.db import models
from django.db.models.base import Model

# Create your models here.
class SignalStrength(models.Model):
  operator_name = models.CharField(max_length=25)
  latitude = models.CharField(max_length=20)
  longitude = models.CharField(max_length=20)
  address = models.CharField(max_length=150, null=True)
  time_added = models.TimeField(auto_now=True)
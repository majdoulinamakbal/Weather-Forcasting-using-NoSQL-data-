
from djongo.models import CheckConstraint, Q
from djongo import models
from pymongo.read_concern import ReadConcern




class Weather(models.Model):
    time = models.FloatField()
    temperature = models.FloatField()
    humidite = models.IntegerField()
    vent = models.IntegerField()
    def time_float(self):
        return float(self.time)
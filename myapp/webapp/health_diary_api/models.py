from django.db import models
from django.contrib.auth.models import User
import datetime


class HealthDiary(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    weigth = models.FloatField(null=True)
    rest_hr = models.IntegerField(null=True)
    morning_sress_score = models.IntegerField(null=True)
    evening_stress_score = models.IntegerField(null=True)
    moring_mood = models.IntegerField(null=True)
    evening_mood = models.IntegerField(null=True)
    sleep_length = models.DateTimeField(null=True)

from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    main_sport = models.CharField(max_length=15)
    heigth = models.IntegerField(null=True)
    ftp = models.IntegerField(null=True)
    max_hr = models.IntegerField(null=True)
    hr_zones = models.CharField(max_length=50, null=True)
    pw_zones = models.CharField(max_length=50, null=True)
    lactate_thr = models.IntegerField(null=True)

    def __str__(self) -> str:
        return str(self.user.username) + ' profile'

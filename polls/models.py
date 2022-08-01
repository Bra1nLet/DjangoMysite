from django.db import models


# Create your models here.
class Userr(models.Model):
    Login = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)
    Nickname = models.CharField(max_length=25)
    Vallue = models.PositiveIntegerField(max_length=30, default=0)
    Valluepr = models.PositiveIntegerField(max_length=15, default=0)
    Build1 = models.PositiveIntegerField(max_length=6, default=0)
    Build2 = models.PositiveIntegerField(max_length=6, default=0)

    def __str__(self):
        return self.Nickname

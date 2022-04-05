from django.db import models

from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime

class CartDetails(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    movie_name= models.CharField(max_length=120,blank=False)






    def __str__(self):
        return  self.client + " - " + self.movie_name
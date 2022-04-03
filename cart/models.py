from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime

class CartDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    movie_name= models.TextField(blank=False)
    price_ht = models.FloatField(default=20)


    TAX_AMOUNT = 19.25

    def price_ttc(self):
        return self.price_ht * (1 + CartDetails.TAX_AMOUNT/100.0)

    def __str__(self):
        return  self.client + " - " + self.movie_name
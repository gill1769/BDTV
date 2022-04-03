from django.db import models
from django.contrib.auth.models import User
from django.utils.datetime_safe import datetime

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    movie_name= models.TextField(blank=False)
    price_ht = models.FloatField(default=20)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)

    TAX_AMOUNT = 19.25

    def price_ttc(self):
        return self.price_ht * (1 + Cart.TAX_AMOUNT/100.0)

    def __str__(self):
        return  self.client + " - " + self.movie_name
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Team(models.Model):
    harji = models.ImageField(default='harji.jpeg', upload_to='profile_pics')
    sai = models.ImageField(default='sai.jpeg', upload_to='profile_pics')
    sandy = models.ImageField(default='sandy.jpeg', upload_to='profile_pics')
    ak = models.ImageField(default='Ak.jpeg', upload_to='profile_pics')
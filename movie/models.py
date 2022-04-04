import json

import requests
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_released = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def getMovie(cls,title):

        url = "https://imdb-data-searching.p.rapidapi.com/om"
        querystring = {"t": title}
        headers = {
            "X-RapidAPI-Host": "imdb-data-searching.p.rapidapi.com",
            "X-RapidAPI-Key": "3249b2a687mshcab474fd48b5de5p147250jsn06cd5b32b0ef"
        }

        response = requests.request("GET", url, headers=headers, params=querystring)
        data = json.loads(response.text)
        #parser_classes = (parsers.JSONParser,)
        cls.movieData = {}
        cls.movieData['Title'] = data['Title']
        cls.movieData['Actors'] = data['Actors'].split(' , ')
        cls.movieData['Language'] = data['Language'].split(' , ')
       # cls.movieData['Rated'] = data['Rated']
        cls.movieData['Released'] = data['Released']
        cls.movieData['Plot'] = data['Plot']
        cls.movieData['Writer'] = data['Writer'].split(' , ')
        cls.movieData['Director'] = data['Director']
        cls.movieData['Runtime'] = data['Runtime']
        cls.movieData['Poster'] = data['Poster']
        return cls.movieData


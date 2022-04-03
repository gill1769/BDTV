import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
import json
from users.forms import AboutRegsiter

def home(request):
    return render(request, 'movie/home.html')


def about(request):
    form=AboutRegsiter()
    return render(request, 'movie/about.html',{'form':form})

def new(request):
    test='Django Unchained'
    movie=Movie()
    re= movie.getMovie(test)

    return render(request,'movie/about.html',{'movies':re})
import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
import json
from users.forms import AboutRegsiter
from movie.forms import SearchForm

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

def search(request):
    form = SearchForm()
    re=''
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            movie = Movie()
            re = movie.getMovie(title)

    # return redirect(home)
    return render(request, 'movie/search_result.html', {'form': form,'re':re})
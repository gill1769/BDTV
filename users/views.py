from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from movie.views import home


def register(request):
    form = UserRegisterForm()
    #return redirect(home)
    return render(request, 'users/register.html', {'form':form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')

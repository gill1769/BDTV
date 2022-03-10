from django.shortcuts import render, redirect
from .models import Movie
from users.forms import AboutRegsiter

def home(request):
    return render(request, 'movie/home.html')


def about(request):
    form=AboutRegsiter()
    return render(request, 'movie/about.html',{'form':form})

def new(request):
    return redirect('https://www.google.com/search?q=batman+2022&rlz=1C1CHBF_enIN926IN926&sxsrf=APq-WBut6TGtDPyHZSdILaEP5jNpAQggBA%3A1646848681933&ei=qeooYp_QOIm7tAbs6pLQDA&ved=0ahUKEwjfyL21zbn2AhWJHc0KHWy1BMoQ4dUDCA4&uact=5&oq=batman+2022&gs_lcp=Cgdnd3Mtd2l6EAMyCwguELEDEIMBEJECMgsIABCxAxCDARCRAjIQCAAQgAQQhwIQsQMQgwEQFDILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMggIABCABBCxAzILCAAQgAQQsQMQgwE6BwgAEEcQsAM6BwgAELADEEM6CggAEOQCELADGAA6DwguENQCEMgDELADEEMYAToMCC4QyAMQsAMQQxgBOg0ILhCxAxCDARDUAhBDOgoILhCxAxCDARBDOgoIABCxAxCDARBDOgcILhDUAhBDOgQIABBDOgsILhCABBCxAxCDAUoECEEYAEoECEYYAVCqAljVB2C8CWgBcAF4AIABoQGIAcoEkgEDMS40mAEAoAEByAEQwAEB2gEGCAAQARgJ2gEGCAEQARgI&sclient=gws-wiz')
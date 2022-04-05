from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('new/', views.new, name='new'),
    path('search/',views.search,name='search'),
    path('movie_details/<movie_id>/',views.movie_detail,name='movie_details'),
    path('payment/',views.payment,name='payment'),
    path('trailers/',views.trailers,name='trailers')
]

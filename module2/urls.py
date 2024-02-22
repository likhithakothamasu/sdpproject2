from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', url_shortener, name='url_shortener'),
    path('<str:short_url>/', redirect_to_original, name='redirect_to_original'),
]
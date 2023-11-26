from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.index, name='index'),


    path('compound-interest/', views.compound_interest, name='compound-interest'),
]

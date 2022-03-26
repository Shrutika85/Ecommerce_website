from django.contrib import admin
from django.urls import path
from . import views
from AI_module import views

urlpatterns = [
    path('', views.home, name='home'),
path('try', views.getOrderPage)
]

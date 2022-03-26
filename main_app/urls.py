from django.contrib import admin
from django.urls import path
from . import views
from main_app import views

urlpatterns = [
    path('', views.home, name='home'),
path('try', views.getOrderPage),
path('Aboutus', views.getAboutPage),
path('Login', views.getLoginPage),
path('SignUp', views.getSignUp),
path('products', views.getProducts)
]

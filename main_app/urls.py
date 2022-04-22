from django.contrib import admin
from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home, name='home'),
path('order', views.getOrderPage),
path('Aboutus', views.getAboutPage),
path('Login', views.getLoginPage),
path('SignUp', views.getSignUp),
path('products', views.getProducts),
path('productview', views.getProductsView),
path('wishlist', views.getWishlistPage),
path('bag', views.getBagPage),
path('wishlist_empty', views.getEmptyWishlist),
path('bag_empty', views.getEmptyBag),
path('brands', views.getBrands)
]

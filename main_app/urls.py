from django.contrib import admin
from django.urls import path
from main_app import views
urlpatterns = [
path('SignedIn',views.insertUser),
path('LoggedIn',views.userLogin),
path('', views.home, name='home'),
path('Logout',views.logout),
path('home', views.home, name='home'),
path('order', views.getOrderPage),
path('Aboutus', views.getAboutPage),
path('Login', views.getLoginPage),
path('SignUp', views.getSignUp),
path('products', views.getProducts),
path('productview', views.getProductsView),
path('wishlist', views.getWishlistPage),
path('wishlist_remove', views.getWishlistremoved),
path('cart_remove', views.getCartremoved),
path('bag', views.getBagPage),
path('wishlist_empty', views.getEmptyWishlist),
path('bag_empty', views.getEmptyBag),
path('brands', views.getBrands),
path('feedback', views.insertfeedback)
]


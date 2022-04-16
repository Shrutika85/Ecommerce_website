from django.http import HttpResponse
from django.shortcuts import render
from .models import *
#from PIL import Image
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.db import connection
def home(request):
    brand1=Brand()
    brand1.desc="Globus Dynemically"
    brand1.img="biba.jpeg"

    brand2 = Brand()
    brand2.desc = "Change is beautiful"
    brand2.img = "biba.jpeg"

    brand3 = Brand()
    brand3.desc = "Hennes & Mauritz"
    brand3.img = "h&m.png"

    brand4 = Brand()
    brand4.desc = "Live in Levis"
    brand4.img = "levis.jpeg"
    brands=[brand1, brand2, brand3, brand4]
    return render(request, 'index.html', {'brand1': brands})

def getimage(request):
    #   with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM category_1_car")
    #     row = cursor.fetchone()
    #     print(row)
    # return render(request, 'image.html', context)
        # fileobj=request.FILES['filepath']
        # fs=FileSystemStorage()
        # filePathName=fs.save(fileobj.name, fileobj)
        # filePathName=fs.url(filePathName)
        # context = {'filePathName': filePathName}
    return render(request, 'index.html',)

def getOrderPage(request):
    return render(request,"./order-box.html")

def getAboutPage(request):
    return render(request,"./About us.html")

def getLoginPage(request):
    return render(request,"./Log-in.html")

def getSignUp(request):
    return render(request,"./sign-in.html")

def getProducts(request):
    return render(request,"./products_view.html")

def getProductsView(request):
    return render(request,"./product_details.html")

def getBagPage(request):
    return render(request,"./bag.html")

def getWishlistPage(request):
    return render(request,"./wishlist.html")

def getEmptyWishlist(request):
    return render(request,"./Login(wishlist empty).html")

def getEmptyBag(request):
    return render(request,"./Login(bag empty).html")

def getBrands(request):
    return render(request,"./brand.html")

from django.http import HttpResponse
from django.shortcuts import render
from main_app.models import *
#from PIL import Image
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.db import connection
def home(request, cursor=None):
    for h in brand.objects.all():
        print(h.brand_id)
        print(h.brand_desc)
        print(h.brand_name)
        print(h.brand_image)
    # for x in product.objects.all():
    #     with connection.cursor() as cursor:
    #        cursor.execute('SELECT brand_name from main_app_brand where brand_id='+str(x.product_brand_id))
    #        print(x.product_brand_id)
    #        print(cursor.fetchone())
    return render(request, 'index.html',{'brands': brand.objects.all()})

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

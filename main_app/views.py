from django.http import HttpResponse
from django.shortcuts import render
#from PIL import Image
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.db import connection
def home(request):
    context={'a': 1}
    return render(request, 'index.html', {'name': 'Shreya'})

def getimage(request):
    #   with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM category_1_car")
    #     row = cursor.fetchone()
    #     print(row)
    # return render(request, 'image.html', context)
        print(request)
        # fileobj=request.FILES['filepath']
        # fs=FileSystemStorage()
        # filePathName=fs.save(fileobj.name, fileobj)
        # filePathName=fs.url(filePathName)
        # context = {'filePathName': filePathName}
        return render(request, 'index.html')

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

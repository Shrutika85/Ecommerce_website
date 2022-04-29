from django.http import HttpResponse
from django.shortcuts import render
from main_app.models import *
#from PIL import Image
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.db import connection
def home(request, cursor=None):
    print(request.POST)
    # if request.POST.get('password', None)== request.POST.get('password2', None):
    #     cust1=customer()
    #     cust1.cust_id=1
    #     cust1.cust_name=request.POST.get('username',None)
    #     cust1.cust_email=request.POST.get('useremail', None)
    #     cust1.cust_password=request.POST.get('password', None)
    #     cust1.cust_contact=request.POST.get('contact', None)
    #     cust1.cust_address=request.POST.get('address', None)
    #     print(cust1)
    #     cust1.save()
    # for x in product.objects.all():
    #     with connection.cursor() as cursor:
    #        cursor.execute('SELECT brand_name from main_app_brand where brand_id='+str(x.product_brand_id))
    #        print(x.product_brand_id)
    #        print(cursor.fetchone())
    # data={'0':{'brands': brand.objects.all()},'1':{'category':category.objects.all()}}
    # print(data['0']['brands'],data['1']['category'])
# data={}
    context={'brands':brand.objects.all(),'category':category.objects.all()}
    return render(request, 'index.html',context)

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
    categoryofhome=(request.GET.get('cat_val',None))
    print(categoryofhome)
    context={}
    if categoryofhome=='TOPS':
        bf=cat1.objects.filter(car_name="BestOffers")
        gf = cat1.objects.filter(car_name="Trends")
        context={'bestoffers':bf,'trends':gf}
    elif categoryofhome=='SKIRTS':
        bf = cat2.objects.filter(car2_name="BestOffers")
        gf = cat2.objects.filter(car2_name="Trends")
        context = {'bestoffers': bf, 'trends': gf}
    elif categoryofhome == 'KURTIS':
        bf = cat3.objects.filter(car3_name="BestOffers")
        gf = cat3.objects.filter(car3_name="Trends")
        context = {'bestoffers': bf, 'trends': gf}
    elif categoryofhome == 'SHIRTS':
        bf = cat4.objects.filter(car4_name="BestOffers")
        gf = cat4.objects.filter(car4_name="Trends")
        context = {'bestoffers': bf, 'trends': gf}
    elif categoryofhome == 'T-SHIRTS':
        bf = cat5.objects.filter(car5_name="BestOffers")
        gf = cat5.objects.filter(car5_name="Trends")
        context = {'bestoffers': bf, 'trends': gf}
    elif categoryofhome == 'JEANS':
        bf = cat6.objects.filter(car6_name="BestOffers")
        gf = cat6.objects.filter(car6_name="Trends")
        context = {'bestoffers': bf, 'trends': gf}
    return render(request,"./brand.html",context)

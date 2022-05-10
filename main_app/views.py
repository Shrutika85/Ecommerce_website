from pydoc import resolve
from pyexpat.errors import messages

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from main_app.models import *
from django.core.mail import send_mail
import datetime as dt
#from PIL import Image
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.db import connection
def home(request, cursor=None):
    context = {'brands': brand.objects.all(), 'category': category.objects.all()}
    return render(request, 'index.html',context)

def userLogin(request):
    context = {'brands': brand.objects.all(), 'category': category.objects.all(),"logstatus":True}
    mail = request.POST.get('user_email', None)
    password = request.POST.get('user_password', None)
    if customer.objects.filter(cust_email=mail, cust_pass=password).exists():
        cust=customer.objects.filter(cust_email=mail)
        # isLogin = True
        context.update({"logstatus":True})
        request.session["user_id"]=cust[0].cust_id
        print("you are ",request.session.get("user_id"))
        return render(request, 'index.html', context)
    else:
        context.update({"logstatus": False})
        return render(request, 'Log-in.html', context)

def insertUser(request):
    if request.POST.get('userpass', None) == request.POST.get('password2', None):
        # if not customer.objects.filter(cust_email=request.POST.get('useremail', None).exits()):
        cust1 = customer()
        cust1.cust_name = request.POST.get('username', None)
        cust1.cust_pass = request.POST.get('userpass', None)
        cust1.cust_email = request.POST.get('useremail', None)
        cust1.cust_contact = request.POST.get('contact', None)
        cust1.cust_address = request.POST.get('address', None)
        print(cust1)
        cust1.save()
        context = {'brands': brand.objects.all(), 'category': category.objects.all(),"logstatus":True}
        return render(request, 'index.html', context)
    else:
        print("user is not inserted")
        return render(request, 'sign-in.html')

def logout(request):
    print("you are in logout", request.session.get("user_id"))
    del request.session["user_id"]
    print("i am destroyed ", request.session.get("user_id"))
    return render(request, 'Log-in.html')
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
    return render(request, './index.html',)

def getOrderPage(request):
    if (request.session.has_key('user_id')):
        context = {}
        main_id = (request.GET.get('prod_id', None))
        prod = product.objects.filter(product_id=main_id)[0]
        imgl = product_image.objects.filter(prod_image=main_id)[0].img1
        clr = color.objects.filter(prod_color=main_id)[0].color_name
        prod_desc = product_desc.objects.filter(main_product=main_id)[0]
        cat = category.objects.filter(cat_id=prod.product_cat_id)[0].cat_name
        pd = user_prod(main_id, prod.product_name, prod.product_description, clr, prod_desc.prod_price,prod.product_offer, prod.product_size, imgl)
        print(pd)
        context = {"product": pd}
        name = "Shrutikas "+prod.product_name
        subject = "django mail test"+prod.product_description
        message = f"Dear Shrutika, your order for {prod.product_name} with {prod.product_description} has been successfully placed"
        print(name, subject, message)
        send_mail(
            subject,
            message,
            'clothiify@gmail.com',
            ['mahajanshrutika8@gmail.com'],
            fail_silently=False,
        )
        return render(request,"./order-box.html",context)
    else:
        return render(request,'./not-login.html')

def getAboutPage(request):
    return render(request,"./About us.html")

def getLoginPage(request):
    context={'logstatus':True}
    return render(request,"./Log-in.html",context)

def getSignUp(request):
    return render(request,"./sign-in.html")

def getProducts(request):
    contentType= (request.GET.get('main', None))
    context = {}
    if contentType=='offers':
        productlist = product.objects.filter(product_offer=True)
        prod_l=[]
        for x in productlist:
            id=x.product_id
            name=x.product_name
            desc = x.product_description
            prod_des = product_desc.objects.filter(main_product=id)
            p=prod_des[0].prod_price
            prod_img = product_image.objects.filter(prod_image=id)
            im1=prod_img[0].img1
            p1 =  prod_grid_view(id,name,p,im1,desc)
            prod_l.append(p1)
        context={"prod_list":prod_l}
    elif contentType == 'trends':
        productlist = trends.objects.all()
        print(productlist)
        prod_l = []
        for x in productlist:
            id = x.prod_trend_id
            prods = product.objects.filter(product_id=id)
            name = prods[0].product_name
            desc = prods[0].product_description
            prod_des = product_desc.objects.filter(main_product=id)
            p = prod_des[0].prod_price
            prod_img = product_image.objects.filter(prod_image=id)
            im1 = prod_img[0].img1
            p1 =   prod_grid_view(id,name,p,im1,desc)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'GLOBUS':
        productlist = product.objects.filter(product_brand=1)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'BIBA':
        productlist = product.objects.filter(product_brand=2)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'HandM':
        productlist = product.objects.filter(product_brand=3)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'LEVIS':
        productlist = product.objects.filter(product_brand=4)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,x.product_name,prod_des[0].prod_price,prod_img[0].img1,x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'TOPS_Offers':
        productlist = product.objects.filter(product_cat=1,product_offer=True)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            prod_l.append(  prod_grid_view(id,x.product_name,prod_des[0].prod_price,prod_img[0].img1,x.product_description))
        context = {"prod_list": prod_l}
    elif contentType == 'SKIRTS_Offers':
        productlist = product.objects.filter(product_cat=2,product_offer=True)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            prod_l.append(  prod_grid_view(id,x.product_name,prod_des[0].prod_price,prod_img[0].img1,x.product_description))
        context = {"prod_list": prod_l}
    elif contentType == 'KURTIS_Offers':
        productlist = product.objects.filter(product_cat=3,product_offer=True)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            prod_l.append(  prod_grid_view(id,x.product_name,prod_des[0].prod_price,prod_img[0].img1,x.product_description))
        context = {"prod_list": prod_l}
    elif contentType == 'SHIRTS_Offers':
        productlist = product.objects.filter(product_cat=4,product_offer=True)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            prod_l.append(  prod_grid_view(id,x.product_name,prod_des[0].prod_price,prod_img[0].img1,x.product_description))
        context = {"prod_list": prod_l}
    elif contentType == 'T-SHIRTS_Offers':
        productlist = product.objects.filter(product_cat=5,product_offer=True)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            prod_l.append(  prod_grid_view(id,x.product_name,prod_des[0].prod_price,prod_img[0].img1,x.product_description))
        context = {"prod_list": prod_l}
    elif contentType == 'JEANS_Offers':
        productlist = product.objects.filter(product_cat=6,product_offer=True)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            prod_l.append(  prod_grid_view(id,x.product_name,prod_des[0].prod_price,prod_img[0].img1,x.product_description))
        context = {"prod_list": prod_l}
    elif contentType == 'TOPS_Trends':
        productlist = trends.objects.filter(prod_cat=1)
        prod_l = []
        for x in productlist:
            id = x.prod_trend_id
            prods = product.objects.filter(product_id=id)
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,prods[0].product_name,prod_des[0].prod_price,prod_img[0].img1,prods[0].product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'SKIRTS_Trends':
        productlist = trends.objects.filter(prod_cat=2)
        prod_l = []
        for x in productlist:
            id = x.prod_trend_id
            prods = product.objects.filter(product_id=id)
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,prods[0].product_name,prod_des[0].prod_price,prod_img[0].img1,prods[0].product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'KURTIS_Trends':
        productlist = trends.objects.filter(prod_cat=3)
        prod_l = []
        for x in productlist:
            id = x.prod_trend_id
            prods = product.objects.filter(product_id=id)
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,prods[0].product_name,prod_des[0].prod_price,prod_img[0].img1,prods[0].product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'SHIRTS_Trends':
        productlist = trends.objects.filter(prod_cat=4)
        prod_l = []
        for x in productlist:
            id = x.prod_trend_id
            prods = product.objects.filter(product_id=id)
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,prods[0].product_name,prod_des[0].prod_price,prod_img[0].img1,prods[0].product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'T-SHIRTS_Trends':
        productlist = trends.objects.filter(prod_cat=5)
        prod_l = []
        for x in productlist:
            id = x.prod_trend_id
            prods = product.objects.filter(product_id=id)
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,prods[0].product_name,prod_des[0].prod_price,prod_img[0].img1,prods[0].product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'JEANS_Trends':
        productlist = trends.objects.filter(prod_cat=6)
        prod_l = []
        for x in productlist:
            id = x.prod_trend_id
            prods = product.objects.filter(product_id=id)
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,prods[0].product_name,prod_des[0].prod_price,prod_img[0].img1,prods[0].product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'TOPS_GLOBUS':
        productlist = product.objects.filter(product_brand=1,product_cat=1)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'TOPS_BIBA':
        productlist = product.objects.filter(product_brand=2, product_cat=1)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'TOPS_HandM':
        productlist = product.objects.filter(product_brand=3, product_cat=1)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'TOPS_LEVIS':
        productlist = product.objects.filter(product_brand=4, product_cat=1)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 =   prod_grid_view(id,x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}


    elif contentType == 'SKIRTS_GLOBUS':
        productlist = product.objects.filter(product_brand=1, product_cat=2)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'SKIRTS_BIBA':
        productlist = product.objects.filter(product_brand=2, product_cat=2)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'SKIRTS_HandM':
        productlist = product.objects.filter(product_brand=3, product_cat=2)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'SKIRTS_LEVIS':
        productlist = product.objects.filter(product_brand=4, product_cat=2)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}

    elif contentType == 'KURTIS_GLOBUS':
        productlist = product.objects.filter(product_brand=1, product_cat=3)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'KURTIS_BIBA':
        productlist = product.objects.filter(product_brand=2, product_cat=3)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'KURTIS_HandM':
        productlist = product.objects.filter(product_brand=3, product_cat=3)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'KURTIS_LEVIS':
        productlist = product.objects.filter(product_brand=4, product_cat=3)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}

    elif contentType == 'SHIRTS_GLOBUS':
        productlist = product.objects.filter(product_brand=1, product_cat=5)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'SHIRTS_BIBA':
        productlist = product.objects.filter(product_brand=2, product_cat=5)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'SHIRTS_HandM':
        productlist = product.objects.filter(product_brand=3, product_cat=5)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'SHIRTS_LEVIS':
        productlist = product.objects.filter(product_brand=4, product_cat=5)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'T-SHIRTS_GLOBUS':
        productlist = product.objects.filter(product_brand=1, product_cat=5)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'T-SHIRTS_BIBA':
        productlist = product.objects.filter(product_brand=2, product_cat=5)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'T-SHIRTS_HandM':
        productlist = product.objects.filter(product_brand=3, product_cat=5)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'T-SHIRTS_LEVIS':
        productlist = product.objects.filter(product_brand=4, product_cat=5)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}

    elif contentType == 'JEANS_GLOBUS':
        productlist = product.objects.filter(product_brand=1, product_cat=6)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'JEANS_BIBA':
        productlist = product.objects.filter(product_brand=2, product_cat=6)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'JEANS_HandM':
        productlist = product.objects.filter(product_brand=3, product_cat=6)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    elif contentType == 'JEANS_LEVIS':
        productlist = product.objects.filter(product_brand=4, product_cat=6)
        prod_l = []
        for x in productlist:
            id = x.product_id
            prod_des = product_desc.objects.filter(main_product=id)
            prod_img = product_image.objects.filter(prod_image=id)
            p1 = prod_grid_view(id, x.product_name, prod_des[0].prod_price, prod_img[0].img1, x.product_description)
            prod_l.append(p1)
        context = {"prod_list": prod_l}
    context.update({'brands':brand.objects.all()})
    return render(request, "./products.html", context)
def insertfeedback(request):
    mail = request.GET.get('email', None)
    msg = request.GET.get('feedback', None)
    f=feedback()
    f.desc=msg
    f.email=mail
    if(request.session.has_key('user_id')):
        f.cust_feed_id=request.session.get("user_id")
    f.save()
    return render(request,"./About us.html")

def getProductsView(request):
    context={}
    main_id = (request.GET.get('prod_id',None))
    prod= product.objects.filter(product_id= main_id)[0]
    imgl = product_image.objects.filter(prod_image=main_id)[0]
    clr = color.objects.filter(prod_color=main_id)[0].color_name
    prod_desc = product_desc.objects.filter(main_product=main_id)[0]
    cat=category.objects.filter(cat_id=prod.product_cat_id)[0].cat_name
    pd=prod_view(main_id,prod.product_name,prod.product_description,clr,prod_desc.prod_quanitity,prod.product_size,prod.product_offer,prod_desc.prod_price,cat,imgl.img1,imgl.img2,imgl.img3,imgl.img4)
    print(pd)
    context={"product":pd}
    return render(request,"./product_details.html",context)

def getBagPage(request):
    context = {}
    if (request.session.has_key('user_id')):
        if (request.GET.get('prod_id', None) != None):
            c = cart()
            c.cart_cust_id = request.session.get("user_id")
            c.save()
            ci = cart_item()
            ci.created_on = dt.datetime.now()
            ci.modified_on = dt.datetime.now()
            ci.cart_fk_id = c.cart_id
            ci.product_cart_id = (request.GET.get('prod_id', None))
            ci.save()
        cart_prod = []
        cartobj = cart.objects.filter(cart_cust_id=request.session.get("user_id"))
        for car in cartobj:
            cartlistobj = cart_item.objects.filter(cart_fk_id=car.cart_id)
            for x in cartlistobj:
                main_id = x.product_cart_id
                prod = product.objects.filter(product_id=main_id)[0]
                imgl = product_image.objects.filter(prod_image=main_id)[0].img1
                clr = color.objects.filter(prod_color=main_id)[0].color_name
                prod_desc = product_desc.objects.filter(main_product=main_id)[0]
                cat = category.objects.filter(cat_id=prod.product_cat_id)[0].cat_name
                pd = user_prod(main_id, prod.product_name, prod.product_description, clr, prod_desc.prod_price,
                prod.product_offer, prod.product_size, imgl)
                cart_prod.append(pd)
        if not cart_prod:
            return render(request, "./Login(bag-empty).html")
        context = {"product": cart_prod}
        return render(request, "./bag.html", context)
    else:
        return render(request, './not-login.html')

def getCartremoved(request):
    if (request.session.has_key('user_id')):
        id=request.session.get("user_id")
        prod_id = request.GET.get('prod_id', None)
        cart_item.objects.filter(product_cart_id=prod_id).delete()
    return HttpResponseRedirect('/bag')

def getWishlistPage(request):
    context = {}
    if(request.session.has_key('user_id')):
        if(request.GET.get('prod_id', None)!=None):
            w=wishlist()
            w.wishlist_cust_id=request.session.get("user_id")
            w.save()
            wi = wishlist_item()
            wi.createdon=dt.datetime.now()
            wi.modifiedon=dt.datetime.now()
            wi.wishlist_fk_id=w.wishlist_id
            wi.product_wishlist_id_id=(request.GET.get('prod_id', None))
            wi.save()
        wish_prod=[]
        wishobj=wishlist.objects.filter(wishlist_cust_id=request.session.get("user_id"))
        for wish in wishobj:
            wishlistobj=wishlist_item.objects.filter(wishlist_fk_id=wish.wishlist_id)
            for x in wishlistobj:
                main_id=x.product_wishlist_id_id
                prod = product.objects.filter(product_id=main_id)[0]
                imgl = product_image.objects.filter(prod_image=main_id)[0].img1
                clr = color.objects.filter(prod_color=main_id)[0].color_name
                prod_desc = product_desc.objects.filter(main_product=main_id)[0]
                cat = category.objects.filter(cat_id=prod.product_cat_id)[0].cat_name
                pd = user_prod(main_id, prod.product_name, prod.product_description, clr, prod_desc.prod_price,
                prod.product_offer, prod.product_size, imgl)
                wish_prod.append(pd)
        if not wish_prod:
            return render(request, "./Login(wishlist-empty).html")
        context = {"product":wish_prod}
        return render(request,"./wishlist.html",context)
    else:
        return render(request,'./not-login.html')

def getWishlistremoved(request):
    if (request.session.has_key('user_id')):
        id=request.session.get("user_id")
        prod_id = request.GET.get('prod_id', None)
        wishlist_item.objects.filter(product_wishlist_id_id=prod_id).delete()
    return HttpResponseRedirect('/wishlist')
def getEmptyWishlist(request):
    return render(request, "./Login(wishlist-empty).html")

def getEmptyBag(request):
    return render(request, "./Login(bag-empty).html")

def getBrands(request):
    categoryofhome=(request.GET.get('cat',None))
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
    context.update({'category':categoryofhome,'brands': brand.objects.all()})
    return render(request,"./brand.html",context)

from django.http import HttpResponse
from django.shortcuts import render
#from PIL import Image
from django.core.files.storage import FileSystemStorage
# Create your views here.
from django.db import connection



def home(request):
    context={'a': 1}
    return render(request, 'footer.html', {'name': 'Shreya'})

def getimage(request):
    # with connection.cursor() as cursor:
    #     cursor.execute("SELECT * FROM category_1_car")
    #     row = cursor.fetchone()
    #     print(row)
    #return render(request, 'image.html', context)
        print(request)
        # fileobj=request.FILES['filepath']
        # fs=FileSystemStorage()
        # filePathName=fs.save(fileobj.name, fileobj)
        # filePathName=fs.url(filePathName)
        # context = {'filePathName': filePathName}
        return render(request, 'index.html',)
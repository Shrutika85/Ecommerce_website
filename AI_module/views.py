from django.http import HttpResponse
from django.shortcuts import render
#from PIL import Image
from django.core.files.storage import FileSystemStorage

# Create your views here.
def home(request):
    context={'a':1}
    return render(request, 'home.html', {'name': 'Shreya'})

def getimage(request):
    print(request)
    fileobj=request.FILES['filepath']
    fs=FileSystemStorage()
    filePathName=fs.save(fileobj.name, fileobj)
    filePathName=fs.url(filePathName)
    context = {'filePathName': filePathName}
    return render(request, 'image.html',context)
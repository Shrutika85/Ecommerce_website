from django.http import HttpResponse
from django.shortcuts import render
from PIL import Image

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Shreya'})

def getimage(request):
    #val1 = request.GET(Image.open("filename"))
    f = request.GET.files['image']
    filename = secure_filename(f.filename)
    f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('image.html', form=form )
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from django.core.files.storage import FileSystemStorage
from .predict import model, predict, df, augment_image
from blog.models import Ask2


def index(req):
    return render(req, "ai/detect.html")
    
def prediction(req):
    img = req.FILES["filepath"]
    fs = FileSystemStorage()
    f = fs.save(img.name, img)
    prediction = predict(df, img.name)
    categ = prediction[3]
    categ = categ.lower()
    post = Ask2.objects.filter(question_title=categ)
    return render(req, 'ai/detected.html', {'filepath': fs.url(f), "name" : prediction[0], "symptom" : prediction[1], "remedy" : prediction[2], "post":post})

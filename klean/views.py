from django.shortcuts import render # import django.shortcuts for render html files
from django.http import HttpResponse, HttpResponseRedirect
from formdata.models import Formdata

def homePage(request):
    return render(request, 'index.html')

def aboutPage(request):
    return render(request, 'about.html')
def servicePage(request):
    return render(request, 'service.html')
def projectPage(request):
    return render(request, 'project.html')
def blogPage(request):
    return render(request, 'blog.html')
def blogDetails(request):
    return render(request, 'single.html')
def contactPage(request):
    return render(request, 'contact.html')

def saveForm(request):
    success =""
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        datarcv= Formdata(name=name,email=email,subject=subject,message=message)
        datarcv.save()
        success="successfully inserted"
        return render(request, 'contact.html',{'success':success})
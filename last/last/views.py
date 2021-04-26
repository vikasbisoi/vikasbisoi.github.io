import http.client

from django.shortcuts import render
from . import models
from .models import Contact
from django.http import HttpResponse


def home(request):
    if request.method=='POST':
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()


    return render(request, 'index.html')

'''def contact(request):
    if request.method=='POST':
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return render(request, 'index.html')'''
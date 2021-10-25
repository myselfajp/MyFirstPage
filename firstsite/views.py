from django.shortcuts import render
from django.http import HttpResponse

def http_home(request):
    return render(request,"home.html")

def http_about(request):
    return render(request,"about.html")

def http_contact(request):
    return render(request,"Contact.html")


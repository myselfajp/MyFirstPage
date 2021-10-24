from django.shortcuts import render
from django.http import HttpResponse

def http_home(request):
    return HttpResponse("Home Page")

def http_about(request):
    return HttpResponse("About Page")

def http_contact(request):
    return HttpResponse("Contact Page")


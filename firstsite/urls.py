from .views import *
from django.urls import path

app_name="firstsite"

urlpatterns = [
    path('index',http_home,name='index'),
    path('',http_home),
    path('about',http_about,name='about'),
    path('contact',http_contact,name='contact'),
    path('elements',http_elements,name='elements'),
    path('test',http_test,name='test'),
    path('newsletter',http_newsletter,name='newsletter')
]

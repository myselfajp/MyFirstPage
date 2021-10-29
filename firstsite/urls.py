from .views import http_about, http_blog_home, http_blog_single, http_contact, http_elements, http_home
from django.urls import path

app_name="firstsite"

urlpatterns = [
    path('index',http_home,name='index'),
    path('',http_home),
    path("about",http_about,name='about'),
    path("contact",http_contact,name='contact'),
    path("blog-home",http_blog_home,name='blog-home'),
    path("blog-single",http_blog_single,name='blog-single'),
    path("elements",http_elements,name='elements')
]

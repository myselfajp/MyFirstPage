from .views import http_about, http_blog_home, http_blog_single, http_contact, http_elements, http_home
from django.urls import path

urlpatterns = [
    path('index.html',http_home),
    path('',http_home),
    path("about.html",http_about),
    path("contact.html",http_contact),
    path("blog-home.html",http_blog_home),
    path("blog-single.html",http_blog_single),
    path("elements.html",http_elements)
]

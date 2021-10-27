from .views import http_about, http_contact, http_home
from django.urls import path

urlpatterns = [
    path('',http_home),
    path("about",http_about),
    path("contact",http_contact)
]

from .viwes import http_test
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('http-test',http_test)
]

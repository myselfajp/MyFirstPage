from .views import http_login
from django.urls import path

app_name="accounts"

urlpatterns = [
    
    path("login/",http_login,name='login'),
    
]
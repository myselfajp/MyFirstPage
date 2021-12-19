from .views import http_login,http_logout
from django.urls import path

app_name="accounts"

urlpatterns = [
    
    path("login/",http_login,name='login'),
    path("logout/",http_logout,name='logout'),
    
]
from .views import http_blog_home, http_blog_single
from django.urls import path

app_name="Blog"

urlpatterns = [

    path("blog",http_blog_home,name='blog-home'),
    path("blog/single",http_blog_single,name='blog-single'),

]

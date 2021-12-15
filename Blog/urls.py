from .views import *
from django.urls import path

app_name="Blog"

urlpatterns = [

    path("",http_blog_home,name='blog-home'),
    path("category/<str:cat_name>",http_blog_home,name='blog-category'),
    path("tags/<str:tag_name>",http_blog_home,name='blog-tag'),
    path("post-<str:p1_id>",http_blog_single,name='blog-single'),
    path("test",http_test,name='test-html'),
    path("search/",http_blog_search,name='search')
    
]

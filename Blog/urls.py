from .views import http_blog_home, http_blog_single, http_test ,http_blog_search
from django.urls import path

app_name="Blog"

urlpatterns = [

    path("blog/",http_blog_home,name='blog-home'),
    path("blog/category/<str:cat_name>",http_blog_home,name='blog-category'),
    path("blog/page-<str:p1_id>",http_blog_single,name='blog-single'),
    path("test",http_test,name='test-html'),
    path("serach/",http_blog_search,name='search'),
    
]

from .views import http_blog_home, http_blog_single, http_test
from django.urls import path

app_name="Blog"

urlpatterns = [

    path("blog",http_blog_home,name='blog-home'),
    path("blog/page-<str:p1_id>",http_blog_single,name='blog-single'),
    path("test-<int:p_id>",http_test,name='test-html'),
    
]

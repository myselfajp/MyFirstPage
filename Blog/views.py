from django.shortcuts import render

# Create your views here.
def http_blog_home(request):
    return render(request,"Blog\Blog-home.html")

def http_blog_single(request):
    return render(request,"Blog\Blog-single.html")

from django.http import request
from django.shortcuts import render
from Blog.models import Post
from requests import get
from datetime import datetime

# Create your views here.
def http_blog_home(request):

    #get now time as UTC from API and convert it to datetime_utc type
    get_API=get("http://worldtimeapi.org/api/timezone/Etc/UTC").json()['datetime'][2:19]
    utc_time_now=datetime.strptime(get_API, '%y-%m-%dT%H:%M:%S')

    #make posts list with filter of published_date
    posts=Post.objects.exclude(published_date__gt= utc_time_now)
    context={"posts":posts}

    return render(request,"Blog\Blog-home.html",context)


def http_blog_single(request,p1_id):

    posts=Post.objects.get(id=p1_id)
    posts.counted_views+=1
    posts.save()
    context={"posts":posts}
    return render(request,"Blog\Blog-single.html",context)
    


def http_test(request,p_id):
    posts=Post.objects.get(id=p_id)
    context={"posts":posts}
    return render(request,"Blog\\test.html",context)
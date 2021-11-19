from django.http import request
from django.shortcuts import get_object_or_404, render
from Blog.models import Post
from datetime import datetime,timezone


# Create your views here.
def http_blog_home(request):
    #take nowtime as utc
    utc_time_now=datetime.now(timezone.utc)

    #filter posts by published date and status
    posts=Post.objects.exclude(published_date__gt= utc_time_now).filter(status=1)

    context={"posts":posts}
    return render(request,"Blog\Blog-home.html",context)




def http_blog_single(request,p1_id):
    
    posts=get_object_or_404(Post ,id=p1_id,status=1)
    posts.counted_views+=1
    posts.save()
    
    next_p=Post.objects.filter(id__gt=posts.id, status = 1, published_date__lte =datetime.now(timezone.utc)).order_by('id').first()
    prev_p=Post.objects.filter(id__lt=posts.id, status = 1, published_date__lte =datetime.now(timezone.utc)).order_by('-id').first()

    context={
    "posts":posts,
    "next_p":next_p,
    "prev_p":prev_p
    }
    return render(request,"Blog\Blog-single.html",context)
    



def http_test(request):
    posts=get_object_or_404(Post,id=1)
    context={"posts":posts}
    return render(request,"Blog\\test.html",context)
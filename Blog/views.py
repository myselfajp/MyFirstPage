from django.core import paginator
from django.http import request
from django.shortcuts import get_object_or_404, render
from Blog.models import Post,comment
from datetime import datetime,timezone
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator



# Create your views here.


def http_blog_home(request,**kwargs):
    #take nowtime as utc
    utc_time_now=datetime.now(timezone.utc)
    #filter posts by published date and status
    posts=Post.objects.filter(status=1).order_by("published_date")

    if kwargs.get('cat_name'):
        posts=posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('tag_name'):
        posts=posts.filter(tag__name=kwargs['tag_name'])

    posts = Paginator(posts,2)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context={"posts":posts}
    return render(request,"Blog\Blog-home.html",context)




def http_blog_search(request):
    posts=Post.objects.filter(status=1,published_date__lte =datetime.now(timezone.utc))
    if request.method == 'GET':
        if s:=request.GET.get('s'):

            posts = posts.filter(content__contains=s)
    
    context={'posts':posts}
    return render(request,'Blog/blog-home.html',context)







def http_blog_single(request,p1_id):
    
    posts=get_object_or_404(Post ,id=p1_id,status=1)
    posts.counted_views+=1
    posts.save()
    
    comments=comment.objects.filter(post=p1_id , approved=1)

    next_p=Post.objects.filter(id__gt=posts.id, status = 1, published_date__lte =datetime.now(timezone.utc)).order_by('id').first()
    prev_p=Post.objects.filter(id__lt=posts.id, status = 1, published_date__lte =datetime.now(timezone.utc)).order_by('-id').first()

    context={
    "comments": comments,
    "posts":posts,
    "next_p":next_p,
    "prev_p":prev_p
    }
    return render(request,"Blog\Blog-single.html",context)
    




def http_test(request):
    posts=get_object_or_404(Post,id=1)
    context={"posts":posts}
    return render(request,"Blog\\test.html",context)
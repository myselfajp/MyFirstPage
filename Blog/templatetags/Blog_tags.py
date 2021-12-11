from django import template
from Blog.models import Post,category,tag,comment

register = template.Library()

@register.simple_tag
def plustwo(x):
    return x+2

@register.simple_tag
def CommentCounter(post_id):
    count=comment.objects.filter(post=post_id,approved=1).count()
    return count


@register.filter
def snippet(x,arg=25):
    return x[:arg]

@register.inclusion_tag("Blog/popular-posts.html")
def blog_latest_posts():
    posts=Post.objects.filter(status=1).order_by("-published_date")[0:3]
    return {"posts":posts}

@register.inclusion_tag("Blog/category.html")
def post_categories():
    posts=Post.objects.filter(status=1)
    categories=category.objects.all()
    dic_categories={}
    for name in categories:
        dic_categories[name]=posts.filter(category=name).count()
    return {"categories":dic_categories}

@register.inclusion_tag("Blog/tags.html")
def post_tag():
    tags=tag.objects.all()
    return {"tags":tags}


@register.inclusion_tag("firstsite/latest-post.html")
def latest_posts():
    posts=Post.objects.filter(status=1).order_by("-published_date")[0:6]
    return {"posts":posts}


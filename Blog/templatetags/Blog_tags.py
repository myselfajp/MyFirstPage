from django import template
from Blog.models import Post,category
register = template.Library()

@register.simple_tag
def plustwo(x):
    return x+2

@register.filter
def snippet(x,arg=25):
    return x[:arg]

@register.inclusion_tag("Blog/popular-posts.html")
def latest_posts():
    posts=Post.objects.filter(status=1).order_by("-published_date")
    return {"posts":posts}

@register.inclusion_tag("Blog/category.html")
def post_categories():
    posts=Post.objects.filter(status=1)
    categories=category.objects.all()
    dic_categories={}
    for name in categories:
        dic_categories[name]=posts.filter(category=name).count()
    return {"categories":dic_categories}
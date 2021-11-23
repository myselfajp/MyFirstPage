from django import template
from Blog.models import Post

register = template.Library()

@register.inclusion_tag("firstsite/latest-post.html")
def latest_posts():
    posts=Post.objects.filter(status=1).order_by("-published_date")[0:6]
    return {"posts":posts}
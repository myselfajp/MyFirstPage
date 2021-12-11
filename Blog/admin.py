from django.contrib import admin
from Blog.models import Post,category,tag
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(category)
admin.site.register(tag)
admin.site.register(Post,PostAdmin)
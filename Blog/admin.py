from django.contrib import admin
from Blog.models import Post,category
from django_summernote.admin import SummernoteModelAdmin


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(category)
admin.site.register(Post,PostAdmin)
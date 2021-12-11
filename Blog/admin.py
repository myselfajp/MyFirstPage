from django.contrib import admin
from Blog.models import Post,category,tag,comment
from django_summernote.admin import SummernoteModelAdmin



class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title','author','status')
    list_filter = ('status','author')
    search_fields = ['title','content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('post','name','approved')
    list_filter = ('post','approved')
    search_fields = ['name','post']

# Register your models here.
admin.site.register(category)
admin.site.register(tag)
admin.site.register(comment,CommentAdmin)
admin.site.register(Post,PostAdmin)
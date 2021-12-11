from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from django.urls import reverse

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name
        
class tag(models.Model):
    name=models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(upload_to='Blog/',default='Blog/default.jpg')
    author = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    tag = models.ManyToManyField(tag)
    category = models.ManyToManyField(category)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('Blog:blog-single',kwargs={'p1_id':self.id})

class comment(models.Model):
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    email= models.EmailField()
    subject= models.CharField(max_length=255)
    message= models.TextField()
    created_date= models.DateTimeField(auto_now_add=True)
    updated_date= models.DateTimeField(auto_now=True)
    approved=models.BooleanField(default=False)
    
    
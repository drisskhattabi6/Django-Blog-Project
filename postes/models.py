from django.db import models
from django.contrib.auth.models import User
# from datetime import datetime
 
# User = get_user_model()

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='author_imgs/%y/%m/%d')
 
    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    title = models.CharField(max_length=30)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    # thumbnail = models.ImageField(upload_to='categories_imgs/%y/%m/%d', default='categories_imgs/default/default.png', null=True)
    thumbnail = models.ImageField(upload_to='categories_imgs/%y/%m/%d')
 
    def __str__(self):
        return self.title


class Post(models.Model) :

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField(max_length=300)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='topic_imgs/%y/%m/%d')
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField()
 
    def __str__(self):
        return self.title

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add cannot be changed
    updated_at = models.DateTimeField(auto_now=True) #auto_now can be changed


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    title_tag = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    snippet = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.title

    def publish_time(self):
        db_time = self.post_date
        now = timezone.now()
        seconds = (now - db_time).total_seconds()
        return seconds

class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()

    def __str__(self):
        return self.post.title + " - " + self.body

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(upload_to='images/profile/', blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)


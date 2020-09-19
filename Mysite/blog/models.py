from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField("Category", related_name="posts")

class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
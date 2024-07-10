from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.SET_NULL, null=True)
    comment = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.blog.title

class Like(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    like = models.BooleanField()



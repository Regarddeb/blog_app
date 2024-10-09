from django.db import models
from django.contrib.auth.models import User
from blog_app.models import SoftDeleteModel, TimestampedModel


class BlogPost(SoftDeleteModel, TimestampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
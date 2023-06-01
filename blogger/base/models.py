from django.db import models
from django import forms

# Create your models here.
from django.contrib.auth.models import User

import uuid



class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(null=True, blank=True, max_length=100000000000000000)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.title}"


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE) #one to many relationship means 1 room can have many instances of messages and when a room is deleted its message are also deleted
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True) # every time save method is called go ahead and take a timestamp : auto_now=True, every time save take a sanpashot


    created = models.DateTimeField(auto_now_add=True) # take a timestamp when new room is created
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.body[0:50]
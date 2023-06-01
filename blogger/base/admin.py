from django.contrib import admin

# Register your models here.
from .models import Article, User, Message

admin.site.register(Article)
admin.site.register(Message)
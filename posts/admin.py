from django.contrib import admin
from posts.models import Category, Comment, Post, Tag


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)

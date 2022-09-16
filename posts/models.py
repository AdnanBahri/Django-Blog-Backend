from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name        = "Category"
        verbose_name_plural = "Categories"


class Tag(models.Model):
    name = models.CharField(max_length=100, blank=False, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
        
    class Meta:
        ordering = ["-name"]




class Post(models.Model):
    title       = models.CharField(max_length=255, blank=False, null=False)
    reference   = models.CharField(max_length=255)
    content     = models.TextField(blank=True)
    draft       = models.BooleanField(default=False)

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    owner       = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category    = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")
    tags        = models.ManyToManyField(Tag, blank=True, related_name="posts")
    # comments    = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="posts")


    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering            = ["-created_at"]
        verbose_name        = "Post"
        verbose_name_plural = "Posts"

class Comment(models.Model):
    content     = models.TextField(blank=False, null=False)
    created_at  = models.DateTimeField(auto_now_add=True)

    owner       = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post        = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return '%s - %s' % (self.post.title, self.owner.username)
    

    class Meta:
        ordering            = ["-created_at"]
        verbose_name        = "Comment"
        verbose_name_plural = "Comments"


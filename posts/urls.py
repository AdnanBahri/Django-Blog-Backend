from django.urls import path, include
from .views import ReadCategoryViewSet, TagViewSet, WriteCategoryViewSet, PostViewSet, ReadCommentViewSet, CreateCommentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet, basename="post")
router.register('categories', ReadCategoryViewSet, basename="category")
router.register('create-category', WriteCategoryViewSet, basename="category")
router.register('comments', ReadCommentViewSet, basename="comment")
router.register('create-comment', CreateCommentViewSet, basename="category")
router.register('tags', TagViewSet, basename="comment")



urlpatterns = [
    path('',  include(router.urls)),
]

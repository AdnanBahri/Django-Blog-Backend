from rest_framework import generics, mixins, viewsets, permissions
from posts.models import Post, Category, Comment, Tag
from posts.serializers import (
                            PostSerializer, 
                            CategorySerializer, 
                            CommentSerializer, 
                            ReadCommentSerializer,
                            TagSerializer,
                        )

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    # def get_queryset(self):
    #     return Post.objects.all().filter(owner = self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

class ReadCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

class WriteCategoryViewSet(mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, )


class ReadCommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = ReadCommentSerializer
    permission_classes = (permissions.AllowAny,)


class CreateCommentViewSet(mixins.CreateModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
    

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser, )
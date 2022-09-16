from rest_framework import serializers
from posts.models import Post, Category, Comment, Tag
from users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'content',
            'owner',
            'category',
            'reference',
            'draft',
            'tags',
            'comments',
        )
        read_only_fields = ('owner','comments',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'owner', 'post']
        read_only_fields = ('owner',)

class ReadCommentSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'owner']
        read_only_fields = fields

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

# class WritePostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['title', 'content', "reference", "draft", "category"]


# class ReadPostSerializer(serializers.ModelSerializer):

#     owner = UserSerializer()
#     comments = CommentSerializer(many=True)
#     category = CategorySerializer()

#     class Meta:
#         model = Post
#         fields = (
#             'id',
#             'title',
#             'content',
#             'owner',
#             'category',
#             'reference',
#             'draft',
#             'comments',
#         )
#         read_only_fields = fields
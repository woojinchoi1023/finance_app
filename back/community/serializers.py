from rest_framework import serializers
from .models import Article, Comment, Article_Likes, Comment_Likes
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields='__all__'
        read_only_fields=('article',)

class ArticleLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article_Likes
        fields='__all__'
        read_only_fields=('user','article',)

class CommentLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment_Likes
        fields='__all__'
        read_only_fields=('user','comment',)

class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    article_likes_set = ArticleLikesSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
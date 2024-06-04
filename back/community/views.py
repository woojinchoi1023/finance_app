from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ArticleSerializer, CommentSerializer, ArticleLikesSerializer, CommentLikesSerializer
from .models import Article, Comment, Article_Likes, Comment_Likes
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404



# Create your views here.
@api_view(['GET', 'POST'])
def article(request):
    if request.method == 'GET': # all article list
        articles = Article.objects.all()
        serializers = ArticleSerializer(articles, many=True)
        return Response(serializers.data)
    elif request.method=='POST': # make article
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT','DELETE'])
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'GET': # get detail
        serializers = ArticleSerializer(article)
        return Response(serializers.data)
    elif request.method == 'PUT': # update
        if request.user == article.user:
            serializer = ArticleSerializer(article, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save() 
                return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=='DELETE': # delete
        if request.user == article.user:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'message':'disallowed'})

@api_view(['POST'])
def comment(request, article_id): # create comment
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_id)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def comment_detail(request, article_id, comment_id):
    article = get_object_or_404(Article, pk=article_id)
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'PUT':
        if request.user == comment.user:
            serializer = CommentSerializer(comment, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save() 
                return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    return Response({'message':'disallowed'})

@api_view(['GET', 'POST'])
def article_like(request, article_id): # 게시글 좋아요 정보 + 좋아요 했는지 여부 반환
    likes = Article_Likes.objects.filter(article_id=article_id)
    user = request.user
    if likes.filter(user=user).exists():
        hasLiked = True
    else:
        hasLiked = False
    if request.method=='GET':
        serializer = ArticleLikesSerializer(likes,many=True)
        return Response({'likes':serializer.data, 'hasLiked': hasLiked})
    if request.method == 'POST':
        # user가 좋아요 했으면 좋아요 취소
        # 없으면 좋아요 추가
        if hasLiked:
            likes.filter(user=user).delete()
            likes = Article_Likes.objects.filter(article_id=article_id)
            serializer = ArticleLikesSerializer(likes,many=True)
            return Response({'likes':serializer.data, 'hasLiked': False}) 
        else:
            Article_Likes.objects.create(article_id=article_id, user=user)
            likes = Article_Likes.objects.filter(article_id=article_id)
            serializer = ArticleLikesSerializer(likes,many=True)
            return Response({'likes':serializer.data, 'hasLiked': True}) 
        
@api_view(['GET', 'POST'])
def comment_like(request, article_id, comment_id):
    likes = Comment_Likes.objects.filter(comment_id=comment_id)
    user = request.user
    if likes.filter(user=user).exists():
        hasLiked = True
    else:
        hasLiked = False
    if request.method=='GET':
        serializer = CommentLikesSerializer(likes,many=True)
        return Response({'likes':serializer.data, 'hasLiked': hasLiked})
    if request.method == 'POST':
        if hasLiked:
            likes.filter(user=user).delete()
            likes = Comment_Likes.objects.filter(comment_id=comment_id)
            serializer = CommentLikesSerializer(likes,many=True)
            return Response({'likes':serializer.data, 'hasLiked': False}) 
        else:
            Comment_Likes.objects.create(comment_id=comment_id, user=user)
            likes = Comment_Likes.objects.filter(comment_id=comment_id)
            serializer = CommentLikesSerializer(likes,many=True)
            return Response({'likes':serializer.data, 'hasLiked': True}) 

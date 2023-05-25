from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment
from accounts.models import User

from django.http import HttpResponseForbidden



@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
# @permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        # print(serializer.data)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        token_query = Token.objects.filter(user_id=article.user_id)
        token = token_query.values_list('key', flat=True)[0]

        if token != request.headers.get('Authorization').split(' ')[1]:
            return HttpResponseForbidden('Invalid token')
        else:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(content = request.data)
            return Response(serializer.data)


@api_view(['GET'])
def comment_list(request, article_pk):
    if request.method == 'GET':
        comments = get_list_or_404(Comment, article=article_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    

@api_view(['PUT', 'DELETE'])
def comment_delete(request, comment_pk):
    try:
        comment = get_list_or_404(Comment, pk=comment_pk)
    
        print(111111111111111111111111111)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
        print(22222222222222222222222222)
        if comment.user == request.user:
            print(3333333333333333333333)
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            print(444444444444444444444444444444)
            return HttpResponseForbidden('Invalid token')
        

    # elif request.method == 'PUT':
    #     serializer = CommentSerializer(comment, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)



@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    serializer = CommentSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

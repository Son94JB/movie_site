
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment



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
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def comment_list(request, article_pk):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment, article=article_pk)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)
    
    # elif request.method == 'PUT':
    #     serializer = CommentSerializer(comment, data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data)

    # elif request.method == 'DELETE':
    #     comment.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def comment_create(request, article_pk):
    print('==================================================================')
    print('일단 POST요청은 들어왔어요')
    print('==================================================================')
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, article_pk=article_pk)
    print('==================================================================')
    print('article 변수받아옴')
    print('==================================================================')
    serializer = CommentSerializer(data=request.data)
    print('==================================================================')
    print('serializer 변수받아옴')
    print('==================================================================')
    if serializer.is_valid(raise_exception=True):
        print('==================================================================')
        print('!!serializer valid함!!')
        print('==================================================================')
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

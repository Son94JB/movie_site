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
from dj_rest_auth.models import TokenModel  # 설문

from polls.models import Poll  # 설문

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
            serializer.save(user=request.user)
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
            serializer.save(content=request.data)
            return Response(serializer.data)


@api_view(['GET', 'POST'])  # 게시글 가져오기(리스트), 생성
def comment_basic(request, article_pk):
    if request.method == 'GET':
        comments = get_list_or_404(Comment, article=article_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_change(request, comment_id):
    if request.method == 'DELETE':
        try:
            comment = get_object_or_404(Comment, pk=comment_id)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if comment.user == request.user:
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return HttpResponseForbidden('Invalid token')

    elif request.method == 'PUT':
        comment = get_object_or_404(Comment, pk=comment_id)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# 영화 추천 로직
# 1. 토큰을 받아온다. 받아온 토큰으로 유저 아이디를 가져온다.
# 2. 가져온 유저 아이디와 폴의 유저 아이디 중 일치하는 것을 찾는다
# 3, 일치하는 폴 아이디로 장르 아이디들을 추출한다.
# 4, 장르 아이디들로 영화들 중 같은 장르 아이디를 가진 영화들을 추출
# 5, 추출한 영화 모음을 뷰로 보내준다
@api_view(['GET'])
def recommend(request):
    # 1. 토큰을 받아온다. 받아온 토큰으로 유저 아이디를 가져온다.
    user_token = request.headers.get('Authorization').split(' ')[1]
    token_model = TokenModel.objects.filter(key=user_token).first()

    if token_model:
        user_id = token_model.user_id
        # 2. 가져온 유저 아이디와 폴의 유저 아이디 중 일치하는 것을 찾는다
        polls = Poll.objects.filter(user_id=user_id)
        # 3, 일치하는 폴 아이디로 장르 아이디들을 추출한다.
        my_genre = polls.values_list('key', flat=True)[0]
        # 4, 장르 아이디들로 영화들 중 같은 장르 아이디를 가진 영화들을 추출

        # 5, 추출한 영화 모음을 뷰로 보내준다
        return Response({'user_id': user_id}, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

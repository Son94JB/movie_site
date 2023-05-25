from django.shortcuts import render
from movies.models import Genre
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GenreSerializer, PollSerializer
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class GenresList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    
class CreatePoll(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        serializer = PollSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            print(serializer)
            return Response(serializer.data)
        return Response(serializer.errors)
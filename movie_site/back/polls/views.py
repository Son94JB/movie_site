from django.shortcuts import render
from movies.models import Genre
from .models import Poll
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import GenreSerializer, PollSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class GenresList(APIView):
    def get(self, request):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)
    
class CreatePoll(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        poll = Poll.objects.create(user=request.user)
        print(request.data)
        poll.genre.set(request.data)
        poll.save()
        serializer = PollSerializer(poll)
        return Response(serializer.data)

    # def post(self, request):
    #     serializer = PollSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.genre.set(request.data['genre'])
    #         serializer.save(user=request.user)
    #         return Response(serializer.data)
    #     return Response(serializer.errors)
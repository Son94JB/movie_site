from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Actor, Director
from .serializers import MovieSerializer, MovieDetailSerializer
import requests
from .youtubetrailer import get_movie_trailer
from django.http import JsonResponse
from django.core import serializers
import json
from rest_framework.decorators import api_view
from asgiref.sync import async_to_sync
import asyncio, asgiref
# get_object_or_404 임포트
from django.shortcuts import get_object_or_404
import requests

class MovieListView(APIView):
    def get(self, request, search_term):             
        # 검색 단어로 영화를 검색
        url = f"https://api.themoviedb.org/3/search/movie?query={search_term}&include_adult=false&language=ko-KR&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
        }

        response = requests.get(url, headers=headers)
        response = response.json()

        movies_list = []
        
        # 검색결과(response) 리스트에서 개별 영화 정보를 가져옴
        for movie in response["results"]:
            # print(movie)
            id = movie["id"]
            title = movie["title"]
            poster_path = movie["poster_path"]
            genre_ids = movie["genre_ids"]
            overview = movie["overview"]
            # adult = movie["adult"]

            # db에서 받아온 id를 통해 existing_movie를 찾음
            existing_movie = Movie.objects.filter(id=id).first()

            # existing_movie가 있으면 movies_list에 추가
            if existing_movie:
                movies_list.append(existing_movie)
            
            # existing_movie가 없으면 새로운 movie를 생성하고 저장할 것
            else:
                url = f"https://api.themoviedb.org/3/movie/{id}/credits?language=ko-KR"
                credit_response = requests.get(url, headers=headers)
                credit_response = credit_response.json()

                # 배우와 감독 정보를 담을 리스트
                actor_list = []
                director_list = []

                # 배우정보 가져옴
                for cast in credit_response["cast"]:
                    if cast["known_for_department"] == "Acting":
                        actor_data = {
                            "fields": {
                                "id": cast["id"],
                                "name": cast["name"],
                                "profile_path": cast["profile_path"],
                            }
                        }
                        actor = Actor(**actor_data["fields"])
                        actor.save()
                        actor_list.append(actor)

                # 감독정보 가져옴
                for crew in credit_response["crew"]:
                    if crew["job"] == "Director":
                        director_data = {
                            "fields": {
                                "id": crew["id"],
                                "name": cast["name"],
                                "profile_path": cast["profile_path"],
                            }
                        }
                        director = Director(**director_data["fields"])
                        director.save()
                        director_list.append(director) 
                        # print(director)

                # 영화 제목과 YouTube Data API 키를 입력하세요
                movie_title = title
                api_key = 'AIzaSyDqO27_XD1C7soWNsobVyzyaO0LUvidpFA'

                video_title, video_url, video_id = get_movie_trailer(movie_title, api_key)

                # 영화 정보를 담을 딕셔너리
                movie_data = {
                    "id": id,
                    "title": title,
                    "overview": overview,
                    "poster": poster_path,
                    "trailer": video_url,
                    "trailer_id": video_id,
                    # "adult": adult,
                }
                # 영화 객체를 생성하고 저장

                # ManyToMany 필드에 배우와 감독 리스트를 할당
                movie = Movie(**movie_data)
                movie.save()
                movie.genre.set(genre_ids)
                movie.actor.set(actor_list)
                movie.director.set(director_list)
                movie.save()
                movies_list.append(movie)

        serializer = MovieSerializer(movies_list, many=True)
        return Response(serializer.data)

class MovieDetailView(APIView):
    def get(self, request, movie_id):
        # 주어진 movie_id에 해당하는 영화 객체를 가져옴
        movie = Movie.objects.get(pk=movie_id)
        # movie 객체에서 overview, poster, actor, director, genre, title 필드를 가져옴
        overview = movie.overview
        poster = movie.poster
        actors = movie.actor.all()
        directors = movie.director.all()
        genres = movie.genre.all()
        title = movie.title
        trailer = movie.trailer
        trailer_id = movie.trailer_id

        # 배우, 감독 프로필(이름, 사진경로) 담을 리스트
        actor_profile_list = []
        director_profile_list = []

        for actor in actors:
            actor_profile = {
                "id": actor.id,
                "name": actor.name,
                "profile_path": actor.profile_path,
            }
            actor_profile_list.append(actor_profile)
        
        for director in directors:
            director_profile = {
                "id": director.id,
                "name": director.name,
                "profile_path": director.profile_path,
            }
            director_profile_list.append(director_profile)
        # # moviecredit api 호출
        # url = f"https://api.themoviedb.org/3/movie/{movie.id}/credits?language=en-US"

        # headers = {
        #     "accept": "application/json",
        #     "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
        # }

        # response = requests.get(url, headers=headers)
        # response = response.json()

        # # 응답받은 response의 cast의 known_for_department가 Acting인 경우 profile_path를 가져옴
        # if response["cast"]:
        #     for cast in response["cast"]:
        #         if cast["known_for_department"] == "Acting":
        #             actor_data = {
        #                 "name": cast["name"],
        #                 "profile_path": cast["profile_path"],
        #             }
        #             actor_profile_list.append(actor_data)
        
        # if response["crew"]:
        #     for crew in response["crew"]:
        #         if crew["job"] == "Director":
        #             director_data = {
        #                 "name": crew["name"],
        #                 "profile_path": crew["profile_path"],
        #             }
        #             director_profile_list.append(director_data)



        # genre 순회하면서 genre의 name을 가져옴
        # 각 장르들의 name을 가져올 것
        genre_list = []
        for genre in genres:
            genre_list.append(genre.name)
                

        # 가져온 필드들을 하나의 딕셔너리로 만듦
        movie_detail = {
            "title": title,
            "overview": overview,
            "poster": poster,
            "genre": genre_list,
            "actor_profiles": actor_profile_list,
            "director_profiles": director_profile_list,
            "trailer": trailer,
            "trailer_id": trailer_id,
        }
        
        return Response(movie_detail)
    

# ActorDetailView 만들 것
# ActorDetialView 에서는 배우의 사진, 참여한 영화, 참여한 영화의 첫 번째 포스터를 가져올 것
class ActorDetailView(APIView):
    def get(self, request, actor_id):
        # 주어진 actor_id에 해당하는 배우 객체를 가져옴
        actor = Actor.objects.get(pk=actor_id)
        # actor 객체에서 name, profile_path, movie 필드를 가져옴
        name = actor.name
        profile_path = actor.profile_path
        movies = actor.movie_set.all()

        # 배우가 참여한 영화들의 정보를 담을 리스트
        movie_list = []

        # 배우가 참여한 영화들의 정보를 가져옴
        for movie in movies:
            movie_data = {
                "title": movie.title,
                "poster": movie.poster,
                "id": movie.id,
            }
            movie_list.append(movie_data)

        # 가져온 필드들을 하나의 딕셔너리로 만듦
        actor_detail = {
            "name": name,
            "profile_path": profile_path,
            "movies": movie_list,
        }

        return Response(actor_detail)
    
# DirectorDetailView 만들 것
# DirectorDetailView 에서는 감독의 사진, 참여한 영화, 참여한 영화의 첫 번째 포스터를 가져올 것
class DirectorDetailView(APIView):
    def get(self, request, director_id):
        # 주어진 director_id에 해당하는 감독 객체를 가져옴
        director = Director.objects.get(pk=director_id)
        # director 객체에서 name, profile_path, movie 필드를 가져옴
        name = director.name
        profile_path = director.profile_path
        movies = director.movie_set.all()

        # 감독이 참여한 영화들의 정보를 담을 리스트
        movie_list = []

        # 감독이 참여한 영화들의 정보를 가져옴
        for movie in movies:
            movie_data = {
                "title": movie.title,
                "poster": movie.poster,
                "id": movie.id,
            }
            movie_list.append(movie_data)

        # 가져온 필드들을 하나의 딕셔너리로 만듦
        director_detail = {
            "name": name,
            "profile_path": profile_path,
            "movies": movie_list,
        }

        return Response(director_detail)
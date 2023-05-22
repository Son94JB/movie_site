from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Actor, Director
from .serializers import MovieSerializer, MovieDetailSerializer
import requests
from .youtubetrailer import get_movie_trailer
from django.http import JsonResponse
from django.core import serializers
import json

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
                            "model": "movies.actor",
                            "pk": cast["id"],
                            "fields": {
                                "id": cast["id"],
                                "name": cast["name"],
                            }
                        }
                        actor = Actor(**actor_data["fields"])
                        actor.save()
                        actor_list.append(actor)

                # 감독정보 가져옴
                for crew in credit_response["crew"]:
                    if crew["job"] == "Director":
                        director_data = {
                            "model": "movies.director",
                            "pk": crew["id"],
                            "fields": {
                                "id": crew["id"],
                                "name": crew["name"],
                            }
                        }
                        director = Director(**director_data["fields"])
                        director.save()
                        director_list.append(director) 
                        # print(director)

                # 영화 제목과 YouTube Data API 키를 입력하세요
                movie_title = title
                api_key = 'AIzaSyDqO27_XD1C7soWNsobVyzyaO0LUvidpFA'

                video_title, video_url = get_movie_trailer(movie_title, api_key)


                # 영화 정보를 담을 딕셔너리
                movie_data = {
                    "id": id,
                    "title": title,
                    "overview": overview,
                    "poster": poster_path,
                    "trailer": video_url,
                    # "adult": adult,
                }
                # 영화 객체를 생성하고 저장

                # ManyToMany 필드에 배우와 감독 리스트를 할당
                # print(genre_ids)
                # print(actor_list)
                # print(director_list)
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

        # actor 순회하면서 actor의 name을 가져옴
        # 각 배우들의 프로필 사진 가져올 것
        actor_profile_list = []
        for actor in actors:
            
            url = f"https://api.themoviedb.org/3/search/person?query={actor.name}&include_adult=false&language=ko-KR&page=1"

            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
            }

            response = requests.get(url, headers=headers)
            response = response.json()

            # response의 results에서 profile_path를 가져옴
            if "results" in response and len(response["results"]) > 0 and "profile_path" in response["results"][0]:
                profile_path = response["results"][0]["profile_path"]
            
            else:
                profile_path = None
            
            # actor의 name과 profile_path를 actor_data에 담음
            actor_data ={
                "name": actor.name,
                "profile_path": profile_path,
            }



            # actor_profile_list에 actor_data 추가
            # 이제 모든 배우의 프로필 사진이 담긴 리스트가 생긴 것
            actor_profile_list.append(actor_data)
            
        # director 순회하면서 director의 name을 가져옴
        director_profile_list = []
        for director in directors:
            url = f"https://api.themoviedb.org/3/search/person?query={director.name}&include_adult=false&language=ko-KR&page=1"

            headers = {
                "accept": "application/json",
                "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
            }

            response = requests.get(url, headers=headers)
            response = response.json()

            # response의 results에서 profile_path를 가져옴
            if "results" in response and len(response["results"]) > 0 and "profile_path" in response["results"][0]:
                profile_path = response["results"][0]["profile_path"]

            else:
                profile_path = None

            # director의 name과 profile_path를 director_data에 담음
            director_data = {
                "name": director.name,
                "profile_path": profile_path,
            }

            # director_profile_list에 director_data 추가
            # 이제 모든 감독의 프로필 사진이 담긴 리스트가 생긴 것
            director_profile_list.append(director_data)

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
        }
        
        return Response(movie_detail)
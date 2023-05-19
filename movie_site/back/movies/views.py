from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Movie, Actor, Director
from .serializers import MovieSerializer
import requests

class MovieListView(APIView):
    def get(self, request, search_term):
        url = f"https://api.themoviedb.org/3/search/movie?query={search_term}&include_adult=false&language=ko-KR&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
        }

        response = requests.get(url, headers=headers)
        response = response.json()

        movies_list = []

        for movie in response["results"]:
            id = movie["id"]
            title = movie["title"]
            poster_path = movie["poster_path"]
            genre_ids = movie["genre_ids"]
            overview = movie["overview"]

            existing_movie = Movie.objects.filter(id=id).first()

            if existing_movie:
                movies_list.append(existing_movie)

            else:
                url = f"https://api.themoviedb.org/3/movie/{id}/credits?language=ko-KR"
                credit_response = requests.get(url, headers=headers)
                credit_response = credit_response.json()

                actor_list = []
                director_list = []

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
                        # print(actor)

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

                movie_data = {
                    "id": id,
                    "title": title,
                    "overview": overview,
                    "poster": poster_path,
                    "trailer": "trailer",
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
    def get(self, request, pk):
        # 주어진 pk에 해당하는 영화 객체를 가져옴
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

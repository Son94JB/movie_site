import requests
import json
import subprocess

url = "https://api.themoviedb.org/3/genre/movie/list?language=ko"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwNDc5YmFiNjM4NDc5Y2YzOTRmODFkN2Y3NTUzNDljZiIsInN1YiI6IjY0NjMwNjE2ZWY4YjMyMDE1NTU2MGZiNCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UajmXt4iP952FyFvcmrcMSx_hL-kapU475aJR7V3kWg"
}

response = requests.get(url, headers=headers)
# response 를
# {
#         "model": "movies.genre",
#         "pk": 1,
#         "fields": {
#             "name": "genre1"
#         }
#     },
# 형태로 바꾸기
response = response.json()
genre_list = []
for genre in response["genres"]:
    genre_list.append({
        "model": "movies.genre",
        "id" : genre["id"],
        "fields": {
            "name": genre["name"],
        }
    })

with open("movies/fixtures/genres.json", "r", encoding="utf-8") as f:
    movies = json.load(f)
    for movie in movie_list:
        if movie['fields'] not in [m['fields'] for m in movies]:
            movies.append(movie)
        print(movies)

# movies를 파일에 저장
with open("movies/fixtures/movies.json", "w", encoding="utf-8") as f:
    json.dump(movies, f, ensure_ascii=False, indent=4)

subprocess.call(["python", "manage.py", "loaddata", "movies/fixtures/movies.json"])

print("영화가 추가되었습니다.")
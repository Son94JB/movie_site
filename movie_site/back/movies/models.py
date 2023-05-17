from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.models.CharField(max_length=20)

class Genre(models.Model):
    title = models.CharField(max_length=10)

class Director(models.Model):
    director = models.CharField(max_length=10)

class MovieReview(models.Model):
    # MovieReview 모델의 필드들을 정의
    # 내용, 생성일, 수정일, 점수, 영화id, 작성자id
    # 영화id는 Movie 모델과 연결, 작성자id는 User 모델과 연결
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class MovieDetail(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    # poster 필드 추가, 이미지 파일을 저장할 수 있는 FileField 사용
    poster = models.FileField(blank=True, upload_to='posters/')
    # trailer 필드 추가, url 링크를 저장할 수 있는 URLField 사용
    trailer = models.URLField(blank=True)

from django.db import models
from django.conf import settings
# # 영화 목록 모델
# class Movie(models.Model):
#     title = models.CharField(max_length=20)

# 장르 목록 모델
class Genre(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.name

# 감독 목록 모델
class Director(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

# 배우 목록 모델
class Actor(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.name


# 영화 상세정보 모델
class Movie(models.Model):
    title = models.CharField(max_length=20)
    genre = models.ManyToManyField(Genre, related_name='movies')
    actor = models.ManyToManyField(Actor, related_name='movies')
    director = models.ManyToManyField(Director, related_name='movies')
    poster = models.TextField(blank=True)
    trailer = models.TextField(blank=True)
    
# 영화 리뷰 모델
class MovieReview(models.Model):
    # MovieReview 모델의 필드들을 정의
    # 내용, 생성일, 수정일, 점수, 영화id, 작성자id
    # 영화id는 Movie 모델과 연결, 작성자id는 User 모델과 연결
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='moviereviews')

# 영화 상세정보 모델
class MovieDetail(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    # poster 필드 추가, 이미지 파일을 저장할 수 있는 FileField 사용
    poster = models.FileField(blank=True, upload_to='posters/')
    # trailer 필드 추가, url 링크를 저장할 수 있는 URLField 사용
    trailer = models.URLField(blank=True)
    moviereview = models.ForeignKey(MovieReview, on_delete=models.CASCADE, related_name='moviedetails')
    
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    profile_image = models.ImageField(blank=True, upload_to='profile/')
    profile_text = models.TextField(blank=True)
    movies = models.ManyToManyField('movies.Movie', related_name='users')

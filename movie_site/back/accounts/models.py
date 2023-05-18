from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    profile_image = models.ImageField(blank=True, upload_to='profile/')
    profile_text = models.TextField(blank=True)
    movies = models.ManyToManyField('Movie', related_name='users')
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    profile_image = models.ImageField(blank=True, upload_to='profile/')
    profile_text = models.TextField(blank=True)
    movies = models.ManyToManyField('Movie', related_name='users')
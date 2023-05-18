from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class CustomUser(AbstractUser):
    profile_image = models.ImageField(blank=True, upload_to='profile/')
    profile_text = models.TextField(blank=True)
    movies = models.ManyToManyField('movies.Movie', related_name='users')

class Following(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followers')

    def follow(self, user):
        self.following.add(user)

    def unfollow(self, user):
        self.following.remove(user)

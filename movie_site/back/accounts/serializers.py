from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from django.conf import settings

from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    profile_image = serializers.ImageField(blank=True, upload_to='profile/')
    profile_text = serializers.TextField(blank=True)
    movies = serializers.ManyToManyField('movies.Movie', related_name='users')

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()
        data_dict['profile_image'] = self.validated_data.get('profile_image', '')
        data_dict['profile_text'] = self.validated_data.get('profile_text', '')
        data_dict['movies'] = self.validated_data.get('movies', '')
        return data_dict


class CustomUserDetailsSerializer(UserDetailsSerializer):

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + \
            ('profile_image', 'profile_text', 'movies',)
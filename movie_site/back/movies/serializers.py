from rest_framework import serializers
from .models import Movie, MovieReview, Actor, Director


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__' 

class MovieReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieReview
        fields = '__all__'

class MovieDetailSerializer(serializers.Serializer):
    title = serializers.CharField()
    overview = serializers.CharField()
    poster = serializers.CharField()
    genres = serializers.CharField()
    actor_profiles = serializers.ListField(child=serializers.DictField())
    director_profiles = serializers.ListField(child=serializers.DictField())
    trailer = serializers.CharField()
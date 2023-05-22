from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('<str:search_term>/', views.MovieListView.as_view(), name='movie-list'),
    path('detail/<int:movie_id>/', views.MovieDetailView.as_view(), name='movie-detail'),
]

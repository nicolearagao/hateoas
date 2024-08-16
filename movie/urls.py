from django.urls import path
from movie.views import MovieListCreateView, MovieRetrieveUpdateDestroyView, GenreListCreateView, api_root

urlpatterns = [
    path('', api_root, name='api-root'),
    path('movies/', MovieListCreateView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie-detail'),
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
]
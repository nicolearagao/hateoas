from rest_framework import generics
from movie.models import Movie, Genre
from movie.serializers import MovieSerializer, GenreSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class GenreListCreateView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

@api_view(['GET'])
def api_root(request):
    return Response({
        'movies': request.build_absolute_uri('/movies/'),
        'genres': request.build_absolute_uri('/genres/'),
    })


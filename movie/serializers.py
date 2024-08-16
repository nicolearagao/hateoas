from rest_framework import serializers
from movie.models import Movie, Genre

class GenreSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()

    def get_detail(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.get_absolute_url())
        return obj.id

    def get_link(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f"/genres/{obj.id}/")
        return f"/genres/{obj.id}/"

    class Meta:
        model = Genre
        fields = ['id', 'name', 'detail', 'link']


class MovieSerializer(serializers.ModelSerializer):
    detail = serializers.SerializerMethodField()
    genres = GenreSerializer(many=True, read_only=True)
    links = serializers.SerializerMethodField()

    def get_detail(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(obj.get_absolute_url())
        return obj.id

    def get_links(self, obj):
        request = self.context.get('request')
        if request:
            return {
                "self": request.build_absolute_uri(f"/movies/{obj.id}/"),
                "edit": request.build_absolute_uri(f"/movies/{obj.id}/edit/"),
                "delete": request.build_absolute_uri(f"/movies/{obj.id}/delete/"),
            }
        return {
            "self": f"/movies/{obj.id}/",
            "edit": f"/movies/{obj.id}/edit/",
            "delete": f"/movies/{obj.id}/delete/",
        }

    class Meta:
        model = Movie
        fields = ['id', 'title', 'release_year', 'genres', 'detail', 'links']

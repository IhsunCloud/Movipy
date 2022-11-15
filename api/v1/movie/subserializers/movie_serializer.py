# from rest_framework import serializers

# from taggit_serializer.serializers import TagListSerializerField, TaggitSerializer

# from movie.models import Movie
# from star_ratings.models import Rating

# # from api.v1.movie.subserializers.movie_serializer import MovieSerializer


# class MovieSerializer(TaggitSerializer, serializers.ModelSerializer):
#     movie = MovieSerializer()
    
#     rating_total = serializers.SerializerMethodField()
#     rating_count = serializers.SerializerMethodField()
#     rating_average = serializers.SerializerMethodField()

#     class Meta:
#         model = Movie
#         fields = '__all__'

#     def get_rating_total(self, obj):
#         if obj.ratings.exists():
#             return obj.ratings.first().total
#         else:
#             return 0

#     def get_rating_count(self, obj):
#         if obj.ratings.exists():
#             return obj.ratings.first().count
#         else:
#             return 0

#     def get_rating_average(self, obj):
#         if obj.ratings.exists():
#             return obj.ratings.first().average
#         else:
#             return 0
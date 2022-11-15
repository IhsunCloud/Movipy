# from rest_framework import viewsets, permissions, status
# from rest_framework.decorators import action
# from rest_framework.renderers import JSONRenderer
# from rest_framework.response import Response

# from api.v1.movie.subserializers.movie_serializer import MovieSerializer

# from movie.models import Movie

# # Imports For Generate PDF Action -->
# from drf_pdf.response import PDFResponse
# from drf_pdf.renderer import PDFRenderer


# class MovieViewSet(viewsets.ModelViewSet):
# 	queryset = Movie.objects.all()
# 	serializer_class = MovieSerializer
# 	permission_classes = [permissions.IsAuthenticatedOrReadOnly,]
# 	lookup_field = 'slug'

# 	def perform_create(self, serializer):
# 		serializer.save(author=self.request.user)

# 	@action(detail=True, methods=['get'], renderer_classes=[PDFRenderer, JSONRenderer])
# 	def generate_pdf(self, request, *args, **kwargs):
# 		""" Action For Generate PDF. """

# 		pdf = self.get_object()

# 		if not pdf:
# 			return Response(
# 				{'error': 'Not found'},
# 				status=status.HTTP_404_NOT_FOUND
# 			)

# 		return PDFResponse(
# 			pdf=pdf,
# 			file_name='pdf_id',
# 			status=status.HTTP_200_OK
# 		)
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from movie.models import Crew, Genre, Movie, Review, Role


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	empty_value_display = '-empty-'
	fields = (('title','pub_date'), 'director')
	list_display = ('title', 'get_author_name', 'created_at',)
	list_filter = ('title', 'created_at',)
	prepopulated_fields = {'slug': ('title',), }
	ordering = ('-created_at',)

	def get_author_name(self, obj):
		return obj.author.first_name + ' ' + obj.author.last_name
	get_author_name.short_description = 'Author Name'

	def get_changeform_initial_data(self, request):
		get_data = super(MovieAdmin, self).get_changeform_initial_data(request)
		get_data['author'] = request.user.pk
		return get_data


admin.site.register(Crew)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Role)
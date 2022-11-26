from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from movie.models import Actor, Genre, Movie, Review, Role


class ActorInline(admin.TabularInline):
	model = Actor
	extra = 3



class GenreInline(admin.TabularInline):
	model = Genre
	extra = 3
 
 
class ReviewInline(admin.TabularInline):
	model = Review
	extra = 3
 
 
class RoleInline(admin.TabularInline):
	model = Role
	extra = 3


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	classes = ['collapse']
	date_hierarchy = 'created_at'
	empty_value_display = '-empty-'
	list_display = ('title', 'get_author_name', 'created_at',)
	list_filter = ('title', 'created_at',)
	ordering = ('-created_at',)
	prepopulated_fields = {'slug': ('title',)}
	readonly_fields = ('id',)
	inlines = [
		ActorInline,
		GenreInline,
		ReviewInline,
		RoleInline,
	]
	fieldsets = [
		(None,
			{'fields': ['title', 'slug', 'author']},
     	),
		('Data Information',
				{
				'fields': [
						'description',
						'director',
						'actor',
						'pub_date',
						'imdb_rating',
						'budget',
						'trailer',
						'thumbnail',
						'tags',
						'status'
     				],
			},
		)
    ]

	def get_author_name(self, obj):
		return obj.author.first_name + ' ' + obj.author.last_name
	get_author_name.short_description = 'Author Name'

	def get_changeform_initial_data(self, request):
		get_data = super(MovieAdmin, self).get_changeform_initial_data(request)
		get_data['author'] = request.user.pk
		return get_data
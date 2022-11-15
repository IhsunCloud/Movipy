import readtime

from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.shortcuts import reverse
from django.utils.text import slugify 
from django.utils.translation import gettext_lazy as _

from movie.managers import MovieManager

from ckeditor.fields import RichTextField
from hitcount.models import HitCount
from star_ratings.models import Rating
from taggit.managers import TaggableManager


class Movie(models.Model):
	""" Model definition for Movies. """

	STATUS_CHOICES = (
		('D', 'Draft'),
		('P', 'Published'),
	)

	author = models.ForeignKey('accounts.User', on_delete=models.CASCADE, null=True)
	status = models.CharField(_('Status'), max_length=1, default='D', choices=STATUS_CHOICES)
	
	title = models.CharField(_('Title'), max_length=200)
	slug = models.SlugField(_('Slug'), max_length=100, allow_unicode=True, unique=True)
	description = RichTextField(_('Description'), null=True)
	pub_date = models.DateTimeField(_('Published Date'), null=True)
 
	directors = models.ManyToManyField('movie.Actor', through='MovieDirector')
	actors = models.ManyToManyField('movie.Actor', through='MovieActor')
	
	imdb_rating = models.PositiveSmallIntegerField(_('Imdb Rating'), default=0, null=True)
	budget = models.PositiveSmallIntegerField(_('Movie Budget'), default=0, null=True)
	trailer = models.FileField(_('Trailer'), null=True, blank=True)
	thumbnail = models.ImageField(_('Thumbnail'), upload_to="movie/images/", null=True)
	posters = models.ForeignKey('movie.Poster', on_delete=models.SET_NULL, null=True)
	genres = models.ManyToManyField('movie.Genre', related_name='movies')
	role = models.ForeignKey('movie.Role', on_delete=models.SET_NULL, related_name=_('role'))
	reviews = models.ForeignKey('movie.Reviews', on_delete=models.SET_NULL, verbose_name=_('Reviews'))
	tags = TaggableManager()
 
	ratings = GenericRelation(Rating, related_query_name='ratings')
	hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
		related_query_name='hit_count_generic_relation')
	
	created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
	updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
 
	class Meta:
		""" Meta definition of Movies. """
		db_index = True
		order_insertion_by = ['title']
		unique_together = ('movie', 'genre')
		verbose_name = _('Movie')
		verbose_name_plural = _('Movies')
		ordering = ['-created_at']
		
	def __str__(self):
		""" Unicode representation of Movies. """
		return self.title

	def __repr__(self):
		return self.__str__()

	def get_readtime(self):
		""" Calculates the time description takes the average human to read. """ 
		result = readtime.of_text(self.description)
		return result.text
	
	def get_description(self):
		""" Returns the description of the movie. """
		return self.description.lower()

	def get_absolute_url(self):
		return reverse('movie:detail', kwargs={"slug": self.slug})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Movie, self).save(*args, **kwargs)

	objects = MovieManager()
	
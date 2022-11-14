import readtime 

from django.db import models

from django.contrib.contenttypes.fields import GenericRelation

from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify 

from django.shortcuts import reverse

from accounts.models import User
from movie.submodels.crew import Crew
from movie.submodels.genre import Genre

from movie.managers import MovieManager

from hitcount.models import HitCount
from taggit.managers import TaggableManager
from star_ratings.models import Rating

from ckeditor.fields import RichTextField


class Movie(models.Model):
    """ Model definition for Movies. """

    STATUS_CHOICES = (
        ('D', 'Draft'),
        ('P', 'Published'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    title = models.CharField(_('Title'), max_length=200)
    slug = models.SlugField(_('Slug'), max_length=100, allow_unicode=True, unique=True)
    description = RichTextField(_('Description'), null=True)
    trailer = models.FileField(_('Trailer'), null=True, blank=True)
    
    genres = models.ManyToManyField(Genre, related_name='movies')
    crew = models.ManyToManyField(Crew, through='MovieCrew', related_name=_('Crew'))
    role = models.ForeignKey('movie.MovieRole', on_delete=models.CASCADE, related_name=_('MovieRole'))
    
    thumbnail = models.ImageField(_('Thumbnail'), upload_to="movie/images/", null=True)
    ratings = GenericRelation(Rating, related_query_name='ratings')
    status = models.CharField(_('Status'), max_length=1, default='D', choices=STATUS_CHOICES)
    
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')
    
    tags = TaggableManager()

    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        """ Meta definition for Movies. """
        verbose_name = _('Movie')
        verbose_name_plural = _('Movies')
        ordering = ['-created_at']
        # unique_together = ('Movie', 'category')

    def __str__(self):
        """ Unicode representation of Movies. """
        return self.title

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
    
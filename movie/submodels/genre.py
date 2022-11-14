from django.db import models
from django.utils.translation import gettext_lazy as _


class Genre(models.Model):
    """ Model definition for Genre. """
    
    title = models.CharField(_('Title'), max_length=50)
    is_valid = models.BooleanField(_('Is Valid'), default=True)
    
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return self.__str__()
    
    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ('title',)
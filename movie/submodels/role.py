from django.db import models
from django.utils.translation import gettext_lazy as _


class MovieRole(models.Model):
    """ Model definition for a Role. """
    title = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, related_name='Movie')

    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    class Meta:
        """ Meta definition for a Role. """
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'

    def __str__(self):
        """ Unicode representation for a Role. """
        return self.title
    
    def __repr__(self):
        """ Unicode representation for a Role. """
        return self.__str__()
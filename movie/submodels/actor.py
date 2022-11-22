from django.db import models
from django.utils.translation import gettext_lazy as _


def actor_avatar_directory_path(instance, filename):
    return 'actor_poster_{0}{1}'.format(instance.id, filename)

class Actor(models.Model):
    """ Model definition for Actor. """
    
    ROLE = (
        ('A', 'Actor'),
        ('D', 'Director'),
    )
     
    first_name = models.CharField(_('Firstname'), max_length=32, null=True)
    last_name = models.CharField(_('Lastname'), max_length=32, null=True)
    role = models.CharField(_('Role'), choices=ROLE, max_length=1, null=True)
    birthday = models.DateField(_('Birthday'), null=True)
    avatar = models.ImageField(_('Avatar'), upload_to=actor_avatar_directory_path, null=True)
    
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, related_name='actor')
   
    class Meta:
        """ Meta information of the Actor"""
        verbose_name = _('Actor')
        verbose_name_plural = _('Actors')
        ordering = ('-first_name',)
        
    def __str__(self):
        """ Unicode representation of Actors. """
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        """ Unicode representation of Actor. """
        return self.__str__()
    
    @property
    def full_name(self):
        """ Returns fullname of Actor. """
        return f'{self.first_name} {self.last_name}'
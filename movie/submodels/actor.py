from django.db import models
from django.utils.translation import gettext_lazy as _


def actor_poster_directory_path(instance, filename):
    return 'actor_poster_{0}{1}'.format(instance.id, filename)

class Actor(models.Model):
    """ Model definition for Actor. """
    
    ROLE = (
        ('A', 'Actor'),
        ('D', 'Director'),
    )
     
    name = models.CharField(_('Name'), max_length=32, null=True)
    family = models.CharField(_('Family'), max_length=32, null=True)
    role = models.CharField(_('Role'), choices=ROLE, max_length=1, null=True)
    birthday = models.DateField(_('Birthday'), null=True)
    image = models.ImageField(_('Image'), upload_to=actor_poster_directory_path, null=True)
    
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, related_name='actor')
    
    def get_full_name(self):
        return f'{self.name} {self.family}'
from django.db import models
from django.utils.translation import gettext_lazy as _


def actor_avatar_directory_path(instance, filename):
    return 'actor_poster_{0}{1}'.format(instance.id, filename)

class Actor(models.Model):
    """ Model definition for Actor. """
    class ROLE(models.TextChoices):
        ACTOR    = 'AR', _('Actor')
        DIRECTOR = 'DR', _('Director')
     
    first_name = models.CharField(_('Firstname'), max_length=32, null=True)
    last_name = models.CharField(_('Lastname'), max_length=32, null=True)
    birthday = models.DateField(_('Birthday'), null=True)
    avatar = models.ImageField(_('Avatar'), upload_to=actor_avatar_directory_path, null=True)
    role = models.CharField(_('Role'), choices=ROLE.choices, max_length=2, default=ROLE.ACTOR)
    movies = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, related_name='actors', null=True)   
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
    def get_full_name(self):
        """ Returns fullname of Actor. """
        return f'{self.first_name} {self.last_name}'
    
    @property
    def get_directors_fullname(self):
        """ Returns directors fullname. """
        director = self.role in {
            self.DIRECTOR
        }
        return director.first_name + director.last_name
    
    @property
    def get_actors_fullname(self):
        """ Returns actors fullname. """
        actor = self.role in {
            self.role.ACTOR
        }
        return f'{actor.first_name} {actor.last_name}'
    
    @property
    def get_actors_avatar(self):
        """ Returns actors avatar. """
        actor = self.role in {
            self.role.ACTOR
        }
        return actor.avatar
    
    @property
    def get_directors_avatar(self):
        """ Returns directors avatar. """
        director = self.role in {
            self.role.DIRECTOR
        }
        return director.avatar
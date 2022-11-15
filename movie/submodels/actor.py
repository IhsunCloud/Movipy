from django.db import models
from django.utils.translation import gettext_lazy as _


def actor_poster_directory_path(instance, filename):
    return 'actor_poster_{0}{1}'.format(instance.id, filename)

class Actor(models.Model):
    name = models.CharField(_('Name'), max_length=32, null=True)
    family = models.CharField(_('Family'), max_length=32, null=True)
    birthday = models.DateField(_('Birthday'), null=True)
    image = models.ImageField(_('Image'), upload_to=actor_poster_directory_path, null=True)
    
    def get_full_name(self):
        return f'{self.name} {self.family}'
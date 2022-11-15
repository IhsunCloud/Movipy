from django.db import models
from django.utils.translation import gettext_lazy as _


def poster_directory_path(instance, filename):
    """ poster will be uploaded to --> MEDIA_ROOT/movie_<id>/<filename> """
    return 'movie_poster_{0}/{1}'.format(instance.id, filename)


class Poster(models.Model):
    image = models.ImageField(_('Image'), upload_to=poster_directory_path)
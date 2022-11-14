from django.apps import AppConfig
# from django.utils.translation import ugettext_lazy as _


class MovieConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'movie'
    verbose_name = 'movie'
    verbose_name_plural = 'movies'

    def ready(self):
        print(">DEBUG::loading_signals")
        import movie.signals

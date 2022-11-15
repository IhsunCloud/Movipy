from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from movie.subadmins.movie_admin import MovieAdmin

admin.site.site_header = _("Moviepy Admin")
admin.site.site_title = _("Moviepy Admin Portal")
admin.site.index_title = _("Welcome to Moviepy Portal")
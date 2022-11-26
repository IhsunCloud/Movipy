from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from movie.subadmins.movie_admin import MovieAdmin
from movie.models import Actor
from movie.models import Genre
from movie.models import Review
from movie.models import Role


admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Role)

admin.site.site_header = _("Movipy Admin")
admin.site.site_title = _("Movipy Admin Portal")
admin.site.index_title = _("Welcome to Movipy Portal")
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'api'
    verbose_name = _('Api')
    verbose_name_plural = _('Apis')
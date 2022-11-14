from .base import INSTALLED_APPS
from .base import BASE_DIR
import os


# Third-Party Apps -->
INSTALLED_APPS.append('ckeditor'),
INSTALLED_APPS.append('hitcount'),
INSTALLED_APPS.append('mptt'),
INSTALLED_APPS.append('rest_framework'),
INSTALLED_APPS.append('robots'),
INSTALLED_APPS.append('sorl.thumbnail'),
INSTALLED_APPS.append('star_ratings'),
INSTALLED_APPS.append('taggit'),
INSTALLED_APPS.append('taggit_serializer')

# Custom Project -->
INSTALLED_APPS.append('accounts.apps.AccountsConfig'),
INSTALLED_APPS.append('movie.apps.MovieConfig'),

AUTH_USER_MODEL = "accounts.User"

ALLOW_UNICODE_SLUGS = True

# CKEDITOR Configs -->
CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"

AUTH_USER_MODEL = 'accounts.User'

# Rest Framework Configs -->
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}

# Sending Comment Configs -->
COMMENT_ALLOW_ANONYMOUS = True
COMMENT_USE_EMAIL_FIRST_PART_AS_USERNAME = True

# Star Rating Configs -->
STAR_RATINGS_ANONYMOUS = True
STAR_RATINGS_RERATE = False

# Pillow Configs -->
FILE_HANDLER_PILLOW = {
    'output_mode': 'P',
    'content_type': 'image/jpg',
    'file_format': 'jpg',
    'file_extension': 'jpg',
}

# Django Robots Configs -->
ROBOTS_USE_SITEMAP = True
ROBOTS_SITEMAP_URLS = [
    'http://www.mydomain.com/sitemap.xml',
]
ROBOTS_SITEMAP_VIEW_NAME = 'sitemap'

# HTML Minfier Configs -->
HTML_MINIFY = True
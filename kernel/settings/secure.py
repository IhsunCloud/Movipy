from .base import BASE_DIR
from decouple import config
import os


SECRET_KEY = config('SECRET_KEY')

# DATABASE Config -->
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
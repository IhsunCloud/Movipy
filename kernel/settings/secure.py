import os
from decouple import config
from kernel.settings.base import BASE_DIR


SECRET_KEY = config('SECRET_KEY')

# DATABASE Config -->
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
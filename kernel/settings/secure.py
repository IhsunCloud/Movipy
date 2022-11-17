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


# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True 
# 
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# 
# SECURE_SSL_REDIRECT = True
# 
# SECURE_HSTS_SECONDS = 86400
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True


# Send Email Config -->
# EMAIL_HOST = config('EMAIL_HOST')
# EMAIL_PORT = config('EMAIL_PORT')
# EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# EMAIL_USER_LTS = config('EMAIL_USER_LTS')
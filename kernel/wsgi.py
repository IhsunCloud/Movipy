"""
WSGI config for kernel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kernel.settings')

application = get_wsgi_application()


"""
Celery stuff.
"""
# from __future__ import absolute_import
# import os
# from celery import Celery
# from django.conf import settings

"""
Default settings module for the 'celery' program.
"""
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kernel.settings.development')
# app = Celery('kernel')

"""
Using a string here means the worker will not have to
pickle the object when using Windows.
"""
# app.config_from_object('django.conf:settings')
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



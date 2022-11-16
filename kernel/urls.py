"""kernel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('movie/', include('movie.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, re_path, include

from django.conf import settings
from django.conf.urls.static import static

from movie.sitemaps import MovieSitemap


sitemaps = {
        "Movies": MovieSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie.urls')),
    # path('api/', include('api.v1.urls')),  
    path('accounts/', include('accounts.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

    # re_path(r'^robots\.txt/', include('robots.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

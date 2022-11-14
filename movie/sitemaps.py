from django.contrib.sitemaps import Sitemap

from movie.models import Movie


class MovieSitemap(Sitemap):
        changefreq = "weekly"
        priority = 0.9

        def items(self):
                return Movie.objects.all()

        def lastmod(self, obj):
                return obj.updated_at
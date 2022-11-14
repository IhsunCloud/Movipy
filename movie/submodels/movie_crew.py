from django.db import models

from movie.models import Movie
from movie.models import Crew
from movie.submodels.role import MovieRole

class MovieCrew(models.Model):
    """ Model definition for a MovieCrew. """ 
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_crew')
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, related_name='movie_crew')
    role = models.ForeignKey(MovieRole, blank=True, on_delete=models.CASCADE, related_name='movie_crew')    
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        """ Meta definition of MovieCrew. """
        unique_together = ('movie', 'crew', 'role')
        
    
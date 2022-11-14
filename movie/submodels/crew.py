from django.db import models
from django.utils.translation import gettext_lazy as _


class Crew(models.Model):
    """ Model definition of Crew. """
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )
    
    first_name = models.CharField(_('Firstname'), max_length=100)
    last_name = models.CharField(_('Lastname'), max_length=100)
    
    birthday = models.DateField(_('Birthday'), null=True, blank=True)
    gender = models.PositiveSmallIntegerField(_('Gender'), choices=GENDER_CHOICES, default=MALE)
    avatar = models.ImageField(_('Avatar'), upload_to='crew/avatars/', null=True, blank=True)
    
    is_valid = models.BooleanField(_('Is Valid'), default=True)
    
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        verbose_name = _('Crew')
        verbose_name_plural = _('Crews')
        ordering = ('-first_name',)
        
    def __str__(self):
        """ Unicode representation of Crews. """
        return f'{self.first_name} {self.last_name}'

    def __repr__(self):
        """ Unicode representation of Crew. """
        return self.__str__()
    
    @property
    def full_name(self):
        """ Returns fullname of Crew. """
        return f'{self.first_name} {self.last_name}'
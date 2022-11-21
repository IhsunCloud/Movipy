from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from mptt.models import MPTTModel, TreeForeignKey


class Review(MPTTModel):
    """ Model definition of Reviews. """
    STATUS_CHOICES = (
        ('A', 'Approved'),
        ('R', 'Rejected'),
    )
    
    name = models.CharField(_('Fullname'), max_length=200)
    title = models.CharField(_('Title'), max_length=200)
    text = models.TextField(_('Text'), null=True)
    slug = models.SlugField(_('Slug'), max_length=100, allow_unicode=True, unique=True)
    city = models.CharField(_("User's City"), max_length=16)
    
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, related_name=_('movies'))
    
    by = models.ForeignKey(
        'accounts.User', 
        verbose_name=_("By User"), 
        related_name = _('comments'), 
        on_delete=models.PROTECT
    )
    parent = TreeForeignKey(
        'self',
        verbose_name=_('Parent'),
        related_name='children',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)
    
    class Meta:
        """ Meta definition of Reviews. """
        # db_index = True
        # db_table = 'comments'
        # order_insertion_by = ['name']
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        ordering = ('-created_at',)
    
    def __str__(self):
        """ Unique representation of Reviews. """
        return f"{self.name} {self.title[10]}"
    
    def __repr__(self):
        """ Unique representation of Reviews. """
        return self.__str__()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Review, self).save(*args, **kwargs)


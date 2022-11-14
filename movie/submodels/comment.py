from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User
from mptt.models import MPTTModel, TreeForeignKey

from movie.managers import CommentManager


class Comment(MPTTModel):
    """Model definition for Comment."""

    name = models.CharField(_('Name'), max_length=50, unique=True)
    text = models.CharField(_('Text'), max_length=254)
    parent = TreeForeignKey('self', verbose_name=_('Parent'), related_name='children', on_delete=models.CASCADE, null=True, blank=True)
    by = models.ForeignKey(User, verbose_name=_("By User"), related_name = 'comments', on_delete=models.PROTECT)

    created = models.DateTimeField(_("Created"), auto_now_add=True)
    modified = models.DateTimeField(_("Modified"), auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['name']
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
       super(Comment, self).save(*args, **kwargs)

    objects = CommentManager()
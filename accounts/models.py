from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.utils.translation import ugettext_lazy as _ 


class User(AbstractUser):
	""" My Customized User Model. """

	avatar = models.ImageField(upload_to='uploads/avatars/%Y-%m-%d/', null=True)
	bio = models.TextField(null=True)


class Email(models.Model):
	""" Model definition for Emails. """

	email = models.EmailField('Email', null=True)

	def __str__(self):
		return self.email

	class Meta:
		verbose_name = 'Email'
		verbose_name_plural = 'Emails'
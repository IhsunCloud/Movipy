# from django.core.mail import send_mail
# from django.db.models.signals import Movie_save
# from django.dispatch import receiver

# from kernel.settings.secure import EMAIL_HOST_USER

# from accounts.models import Email
# from movie.models import Movie


# @receiver(movie_save, sender=Movie)
# def SendEmail(sender , instance, created, **kwargs):
#     """ Send email to users when create a Movie. """
    
#     if created:
        
#         emails = list(Email.objects.values('email'))
        
#         recepients = []
#         for i in range(0, len(emails)):
#             recepients.append(emails[i]['email'])
#             pass
        
#         send_mail('New Movie on movie', str(instance.title), EMAIL_HOST_USER, recepients, fail_silently=False)
#         pass
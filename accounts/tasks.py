from time import sleep
from celery.decorators import task
from celery.utils.log import get_task_logger
from django.core.mail import EmailMessage

logger = get_task_logger(__name__)


@task(name='debug_task', bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@task(name='send_email_task')
def send_mail_task(subject, message, email_from, recipient_list):
    message = EmailMessage(subject,
        message,
        email_from,
        recipient_list
    )
    
    message.content_subtype = 'html'
    message.send()
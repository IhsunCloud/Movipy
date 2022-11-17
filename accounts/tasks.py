from celery.decorators import task
from celery.utils.log import get_task_logger
from django.core.mail import EmailMessage
from time import sleep

logger = get_task_logger(__name__)

@task(name='send_email_task')
def send_mail_task(subject, message, email_from, recipient_list):
    message = EmailMessage(subject, message, email_from, recipient_list)
    message.content_subtype = 'html'
    message.send()
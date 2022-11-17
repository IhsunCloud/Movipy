from accounts.tasks import send_mail_task, debug_task


# Task 1: Debug Task.
debug_task()


# Task 2: Send Mail.
subject = ''
message = ''
email = 'no-reply@moviepy.com'
recipient_list = [
   '',
   '',
   ''
]

send_mail_task.delay(
   subject,
   message,
   email,
   recipient_list
)
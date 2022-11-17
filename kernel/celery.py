from accounts.tasks import send_mail_task


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
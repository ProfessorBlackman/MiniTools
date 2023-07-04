from celery import shared_task

from utils.send_email import send_email


@shared_task()
def send_email_task(email:str, template:str, subject:str = None, extra: dict = None):
    print(f"Sending email to {email} {template}")
    print(send_email(email, template, subject, extra))

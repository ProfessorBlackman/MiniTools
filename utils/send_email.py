from django.core.mail import send_mail,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings


# function to send email to user after successful otp confirmation
def send_email(email:str, template:str, subject:str = None, **kwargs):
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    html_content = render_to_string(f"{template}", **kwargs)
    text_content = strip_tags(html_content)
    email = EmailMultiAlternatives(subject,
                                   text_content,
                                   from_email,
                                   recipient_list)
    email.attach_alternative(html_content, 'text/html')
    email.send()
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from ..utils.create_otp import create_otp
from ..tasks.send_emails_task import send_email_task
from django.conf import settings

User = get_user_model()


@receiver(post_save, sender=User)
def generate_token_signal(sender, instance, created, **kwargs):
    if created and not instance.is_staff:
        send_email_task.delay((instance.email_address, 'account-confirmation.html',
                               'MiniTools Account Confirmation',
                               {'content': create_otp(instance.email_address),
                                'domain': f'{settings.FRONTEND_DOMAIN}/confirm?email={instance.email_address}'})
                              )

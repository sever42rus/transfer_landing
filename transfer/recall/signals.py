from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from feedback.models import Feedback

from .models import RecallInvite

INVITE_MESSAGE = """
{0}/recall/invite/{1}/
"""


@receiver(post_save, sender=Feedback)
def send_email_invite_recall(sender, instance, **kwargs):
    if instance.performed and instance.in_work:
        recall_invite = RecallInvite.objects.filter(feedback=instance)
        if not recall_invite:
            recall_invite = RecallInvite(feedback=instance)
            message_mail = INVITE_MESSAGE.format(
                settings.SITE, recall_invite.id)
            send_mail_valid = send_mail('Регистрация на сайте', message_mail, settings.EMAIL_HOST_USER, [
                                        instance.email], fail_silently=True)
            if send_mail_valid:
                recall_invite.save()

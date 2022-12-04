from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta

from .models import CustomUser
from .tasks import auto_delete_resume

@receiver(post_save, sender=CustomUser)
def delate_user_resume(sender, instance, **kwargs):
    # print(instance.resume)
    if instance.resume:
        # auto_delete_resume.delay(instance.id)
        auto_delete_resume.apply_async(args=(instance.id,), countdown=120)
        # date = datetime.utcnow() + timedelta(days=24)
        # auto_delete_resume.apply_async(args=(user.id), eta=date)
from celery import shared_task

from .models import CustomUser

@shared_task
def auto_delete_resume(*args, **kwargs):
	user_id = args[0]
	user = CustomUser.objects.get(id=user_id)
	user.delete_resume()
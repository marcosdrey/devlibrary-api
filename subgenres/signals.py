import os
from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import Subgenre


@receiver(post_delete, sender=Subgenre)
def subgenre_post_delete(sender, instance, **kwargs):
    if instance.icon and os.path.isfile(instance.icon.path):
        os.remove(instance.icon.path)

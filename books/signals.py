import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Book


@receiver(post_delete, sender=Book)
def book_post_delete(sender, instance, **kwargs):
    if instance.photo and os.path.isfile(instance.photo.path):
        os.remove(instance.photo.path)

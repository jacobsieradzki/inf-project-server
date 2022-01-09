from django.db import models
from django.dispatch import receiver
from classroomapi.models import Resource
from classroomapi.helper import s3


@receiver(models.signals.post_delete, sender=Resource)
def on_resource_post_delete(sender, instance: Resource, **kwargs):
    s3.delete_resource(instance.id)

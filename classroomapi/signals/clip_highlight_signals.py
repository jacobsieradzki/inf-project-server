from django.db import models
from django.dispatch import receiver
from classroomapi.models import Clip, Highlight, HighlightRect


@receiver(models.signals.post_delete, sender=Clip)
def on_clip_post_delete(sender, instance: Clip, **kwargs):
    if instance.highlight_id:
        Highlight.objects.filter(id=instance.highlight_id).delete()


@receiver(models.signals.post_delete, sender=Highlight)
def on_highlight_post_delete(sender, instance: Highlight, **kwargs):
    HighlightRect.objects.filter(id=instance.bounding_rect_id).delete()

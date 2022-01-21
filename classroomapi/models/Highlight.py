from django.db import models
from classroomapi.models import Course, Resource
from django.utils.translation import gettext_lazy as _


class HighlightRect(models.Model):
    x1 = models.FloatField()
    y1 = models.FloatField()
    x2 = models.FloatField()
    y2 = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    page_number = models.IntegerField(blank=True, default=0)
    parent_rect = models.ForeignKey('classroomapi.Highlight', on_delete=models.CASCADE)


class Highlight(models.Model):

    class HighlightType(models.TextChoices):
        TXT = 'TXT', _('Text')
        IMG = 'IMG', _('Image')

    id = models.BigIntegerField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    title = models.TextField(blank=True)
    emoji = models.TextField(blank=True)
    content = models.TextField(blank=True)
    type = models.CharField(max_length=16, choices=HighlightType.choices, default=HighlightType.TXT)
    bounding_rect = models.ForeignKey(HighlightRect, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.__str__() + " / HIGHLIGHT " + str(self.resource_id) + ": " + self.content




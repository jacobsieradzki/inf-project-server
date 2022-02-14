from django.db import models
from classroomapi.models import Resource


class HighlightRect(models.Model):
    x1 = models.FloatField()
    x2 = models.FloatField()
    y1 = models.FloatField()
    y2 = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    page_number = models.IntegerField(blank=True, default=0)
    parent = models.ForeignKey('classroomapi.Highlight', on_delete=models.CASCADE, blank=True, null=True)


class Highlight(models.Model):
    id = models.BigIntegerField(primary_key=True)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    bounding_rect = models.ForeignKey(HighlightRect, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

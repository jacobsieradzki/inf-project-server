from django.db import models
from classroomapi.models import Course, Resource, Highlight
from django.utils.translation import gettext_lazy as _


class Clip(models.Model):

    class ClipType(models.TextChoices):
        VIDEO_CLIP = 'VIDEO_CLIP', _('Video Clip')
        PDF_PAGE = 'PDF_PAGE', _('PDF Page')
        PDF_CLIP = 'PDF_CLIP', _('PDF Clip')
        NONE = 'NONE', _('None')

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    description = models.CharField(max_length=60, blank=True)
    emoji = models.CharField(max_length=5, blank=True)
    type = models.CharField(max_length=16, choices=ClipType.choices, default=ClipType.NONE)

    start_location = models.IntegerField()
    end_location = models.IntegerField()
    highlight = models.ForeignKey(Highlight, on_delete=models.CASCADE, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.__str__() + " / CLIP_" + self.type + " (" + str(self.id) + ") on " \
               + self.resource.type + ": " + self.resource.name + " (" + str(self.resource.id) + ")"

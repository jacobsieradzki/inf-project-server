from django.db import models
from classroomapi.models import Course, Resource
from django.utils.translation import gettext_lazy as _


class Clip(models.Model):
    class ClipType(models.TextChoices):
        SUBTITLE = 'SUBTITLE', _('Subtitle')
        VIDEO_CLIP = 'VIDEO_CLIP', _('Video Clip')
        PDF_PAGE = 'PDF_PAGE', _('PDF Page')
        PDF_CLIP = 'PDF_CLIP', _('PDF Clip')

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    content = models.TextField()
    description = models.CharField(max_length=60, blank=True)
    type = models.CharField(max_length=16, choices=ClipType.choices, default=ClipType.LECTURE)
    start_location = models.IntegerField()
    end_location = models.IntegerField()

    def __str__(self):
        return self.course.__str__() + " / CLIP: " + self.type + " (" + str(self.id) + ")"

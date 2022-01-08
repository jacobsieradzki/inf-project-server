from django.db import models
from classroomapi.models import Course
from django.utils.translation import gettext_lazy as _


class Resource(models.Model):
    class ResourceType(models.TextChoices):
        VID = 'VID', _('Video')
        YT = 'YT', _('YouTube')
        PDF = 'PDF', _('PDF')
        URL = 'URL', _('URL')
        IMG = 'IMG', _('IMG')

    class StatusType(models.TextChoices):
        PROCESSING = 'PROCESSING', _('Processing')
        READY = 'READY', _('READY')
        ERROR = 'ERROR', _('ERROR')

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=60, blank=True)
    description = models.CharField(max_length=60, blank=True)
    type = models.CharField(max_length=16, choices=ResourceType.choices, default=ResourceType.URL)
    url = models.URLField(max_length=200, blank=True)
    status = models.CharField(max_length=16, choices=StatusType.choices, default=StatusType.READY)

    def __str__(self):
        return self.course.__str__() + " / RESOURCE: " + self.name + " (" + str(self.id) + ")"

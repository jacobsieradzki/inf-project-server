from django.db import models
from classroomapi.models import Course
from django.utils.translation import gettext_lazy as _


class Link(models.Model):
    class LinkType(models.TextChoices):
        EVENT = 'EVENT', _('Event')
        MEETING = 'MEETING', _('Meeting')
        RESOURCE = 'RESOURCE', _('Resource')
        CLIP = 'CLIP', _('Clip')
        LOCATION = 'LOCATION', _('Location')
        COMMENT = 'COMMENT', _('Comment')

    min_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    min_link_id = models.CharField(max_length=20)
    min_link_type = models.CharField(max_length=16, choices=LinkType.choices)
    max_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    max_link_id = models.CharField(max_length=20)
    max_link_type = models.CharField(max_length=16, choices=LinkType.choices)

    def __str__(self):
        return "LINK: [" + self.min_link_type + ":" + self.min_link_id + "] to [" + self.max_link_type + ":" + self.max_link_id + "]"

from django.db import models
from classroomapi.models import Course, Clip
from django.utils.translation import gettext_lazy as _


class Link(models.Model):
    class LinkType(models.TextChoices):
        EVENT = 'EVENT', _('Event')
        RESOURCE = 'RESOURCE', _('Resource')
        CLIP = 'CLIP', _('Clip')
        COMMENT = 'COMMENT', _('Comment')

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    anchor = models.ForeignKey(Clip, on_delete=models.CASCADE, null=True)

    min_link_id = models.CharField(max_length=20)
    min_link_type = models.CharField(max_length=16, choices=LinkType.choices)
    max_link_id = models.CharField(max_length=20)
    max_link_type = models.CharField(max_length=16, choices=LinkType.choices)

    def __str__(self):
        return self.course.__str__() + " / LINK: [" \
               + self.min_link_type + ":" + self.min_link_id \
               + "] to [" \
               + self.max_link_type + ":" + self.max_link_id + "]"

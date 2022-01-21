from django.db import models
from classroomapi import models as _models
from django.utils.translation import gettext_lazy as _


def get_link_id(event, resource, clip):
    if event is not None:
        return event
    elif resource is not None:
        return resource
    elif clip is not None:
        return clip
    return None


def get_link_type(event, resource, clip):
    if event is not None:
        return Link.LinkType.EVENT
    elif resource is not None:
        return Link.LinkType.RESOURCE
    elif clip is not None:
        return Link.LinkType.CLIP
    return None


class Link(models.Model):
    class LinkType(models.TextChoices):
        EVENT = 'EVENT', _('Event')
        RESOURCE = 'RESOURCE', _('Resource')
        CLIP = 'CLIP', _('Clip')
        COMMENT = 'COMMENT', _('Comment')

    course = models.ForeignKey(_models.Course, on_delete=models.CASCADE)
    subtitle = models.ForeignKey(_models.Subtitle, on_delete=models.SET_NULL, null=True, blank=True)

    min_link_event = models.ForeignKey(_models.Event, on_delete=models.CASCADE,
                                       related_name='min_link_event',
                                       null=True, blank=True)
    min_link_resource = models.ForeignKey(_models.Resource, on_delete=models.CASCADE,
                                          related_name='min_link_resource',
                                          null=True, blank=True)
    min_link_clip = models.ForeignKey(_models.Clip, on_delete=models.CASCADE,
                                      related_name='min_link_clip',
                                      null=True, blank=True)

    max_link_event = models.ForeignKey(_models.Event, on_delete=models.CASCADE,
                                       related_name='max_link_event',
                                       null=True, blank=True)
    max_link_resource = models.ForeignKey(_models.Resource, on_delete=models.CASCADE,
                                          related_name='max_link_resource',
                                          null=True, blank=True)
    max_link_clip = models.ForeignKey(_models.Clip, on_delete=models.CASCADE,
                                      related_name='max_link_clip',
                                      null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_min_type(self):
        return get_link_type(self.min_link_event_id, self.min_link_resource_id, self.min_link_clip_id)

    def get_min_id(self):
        return get_link_id(self.min_link_event_id, self.min_link_resource_id, self.min_link_clip_id)

    def get_max_type(self):
        return get_link_type(self.max_link_event_id, self.max_link_resource_id, self.max_link_clip_id)

    def get_max_id(self):
        return get_link_id(self.max_link_event_id, self.max_link_resource_id, self.max_link_clip_id)

    def __str__(self):
        return self.course.__str__() + " / LINK: [" \
               + self.get_min_type() + ":" + str(self.get_min_id()) \
               + "] to [" \
               + self.get_max_type() + ":" + str(self.get_max_id()) + "]" \
               + " (" + str(self.id) + ")"

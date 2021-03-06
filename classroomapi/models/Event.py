from django.db import models
from classroomapi.models import Course, Resource
from django.utils.translation import gettext_lazy as _


class Event(models.Model):
    class EventType(models.TextChoices):
        LECTURE = 'LECTURE', _('Lecture')
        WORKSHOP = 'WORKSHOP', _('Workshop')
        ASSIGNMENT = 'ASSIGNMENT', _('Assignment')

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    primary_resource = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60, blank=True)
    type = models.CharField(max_length=16, choices=EventType.choices, default=EventType.LECTURE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.__str__() + " / EVENT_" + self.type + ": " + self.name + " (" + str(self.id) + ")"

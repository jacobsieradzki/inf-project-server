from django.db import models
from django.db.models import UniqueConstraint
from django.utils.translation import gettext_lazy as _


class Organisation(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Course(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    class Meta:
        app_label = 'classroomapi'
        constraints = [
            UniqueConstraint(fields=['id', 'organisation'], name='course_id')
        ]

    def __str__(self):
        return self.name


class Event(models.Model):

    class EventType(models.TextChoices):
        LECTURE = 'LECTURE', _('Lecture')
        WORKSHOP = 'WORKSHOP', _('Workshop')
        ASSIGNMENT = 'ASSIGNMENT', _('Assignment')

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    type = models.CharField(max_length=16, choices=EventType.choices, default=EventType.LECTURE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Meeting(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Resource(models.Model):

    class ResourceType(models.TextChoices):
        VID = 'VID', _('Video')
        YT = 'YT', _('YouTube')
        PDF = 'PDF', _('PDF')
        URL = 'URL', _('URL')
        IMG = 'IMG', _('IMG')

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    type = models.CharField(max_length=16, choices=ResourceType.choices, default=ResourceType.URL)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.name

# enum
# LinkResourceType
# {
#     EVENT, MEETING, RESOURCE, CLIP, MOMENT, COMMENT
# }
# {
#     "min_organisation_id": "uoedinburgh",
#     "min_course_id": "mlpr",
#     "min_resource_type": LinkResourceType,
#     "*min_resource_id": UUID,
#     "max_organisation_id": "uoglasgow",
#     "max_department_id": "computing",
#     "max_course_id": "ml",
#     "max_resource_type": LinkResourceType,
#     "*max_resource_id": UUID,
# }

# class Link(models.Model):
#
#     class LinkType(models.TextChoices):
#         EVENT = 'EVENT', _('Event')
#         MEETING = 'MEETING', _('Meeting')
#         RESOURCE = 'RESOURCE', _('Resource')
#
#
from django.db import models
from classroomapi.models import Organisation, Course
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Membership(models.Model):
    class RoleType(models.TextChoices):
        STAFF = 'STAFF', _('Staff')
        STUDENT = 'STUDENT', _('Student')

    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=16, choices=RoleType.choices, default=RoleType.STUDENT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.__str__() + " / MEMBERSHIP " + "_" + self.role + ": " + self.user.username

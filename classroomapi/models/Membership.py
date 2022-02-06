from django.db import models
from classroomapi.models import Course
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Membership(models.Model):
    class MembershipType(models.TextChoices):
        ORGANISATION = 'ORGANISATION', _('Organisation')
        COURSE = 'COURSE', _('Course')

    class RoleType(models.TextChoices):
        STAFF = 'STAFF', _('Staff')
        STUDENT = 'STUDENT', _('Student')

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    membership = models.CharField(max_length=16, choices=MembershipType.choices, default=MembershipType.COURSE)
    role = models.CharField(max_length=16, choices=RoleType.choices, default=RoleType.STUDENT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.__str__() + " / MEMBERSHIP " + self.membership + "_" + self.role + ": " + self.user.username

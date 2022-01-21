from django.db import models
from classroomapi.models import Course, Resource


class Subtitle(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    start_seconds = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.course.__str__() + " / RESOURCE " + str(self.resource_id) \
               + " / " + " @" + str(self.start_seconds) + "s: " + self.content

from django.db import models
from classroomapi.models import Course, Resource


class Subtitle(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    start_seconds = models.IntegerField()

    def __str__(self):
        return self.course.__str__() + " / SUBTITLE: " + self.type + " (" + str(self.id) + ")"

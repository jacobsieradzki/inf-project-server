from django.db import models
from django.db.models import UniqueConstraint
import Organisation


class Course(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        constraints = [
            UniqueConstraint(fields=['id', 'organisation'], name='course_id')
        ]

    def __str__(self):
        return self.name

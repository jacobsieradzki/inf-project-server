from django.db import models
from . import Organisation


class Course(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    organisation = models.ForeignKey(Organisation, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.organisation.__str__() + "/" + self.name

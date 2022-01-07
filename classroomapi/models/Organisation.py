from django.db import models


class Organisation(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name + " (" + self.id + ")"

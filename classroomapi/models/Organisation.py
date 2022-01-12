from django.db import models


class Organisation(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=60)
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name + " (" + self.id + ")"

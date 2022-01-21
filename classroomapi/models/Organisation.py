from django.db import models


class Organisation(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=60)
    image_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " (" + self.id + ")"

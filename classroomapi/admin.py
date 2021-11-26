from django.contrib import admin
from classroomapi import models

admin.site.register(models.Organisation)
admin.site.register(models.Course)
admin.site.register(models.Event)
admin.site.register(models.Meeting)
admin.site.register(models.Resource)

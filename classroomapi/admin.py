from django.contrib import admin
from classroomapi import models, legacy_models

admin.site.register(models.Organisation)
admin.site.register(models.Course)
admin.site.register(legacy_models.Event)
admin.site.register(legacy_models.Meeting)
admin.site.register(legacy_models.Resource)

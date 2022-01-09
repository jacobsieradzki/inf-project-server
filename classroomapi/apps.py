from django.apps import AppConfig


class ClassroomapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classroomapi'

    def ready(self):
        from classroomapi import signals

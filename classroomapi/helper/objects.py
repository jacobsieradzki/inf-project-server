from classroomapi import models


def get_event(obj_id) -> models.Event:
    try:
        return models.Event.objects.get(id=obj_id)
    except models.Event.DoesNotExist:
        return None


def get_resource(obj_id) -> models.Resource:
    try:
        return models.Resource.objects.get(id=obj_id)
    except models.Resource.DoesNotExist:
        return None


def get_clip(obj_id) -> models.Clip:
    try:
        return models.Clip.objects.get(id=obj_id)
    except models.Clip.DoesNotExist:
        return None

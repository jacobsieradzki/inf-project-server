from functools import reduce

from django.db.models import QuerySet
from rest_framework.utils.serializer_helpers import ReturnDict
from classroomapi.models import Link, Event, Resource, Clip
from classroomapi.serializers.event_serializer import EventSerializer
from classroomapi.serializers.resource_serializer import ResourceSerializer
from classroomapi.serializers.clip_serializer import ClipDetailSerializer


def get_link_object(link_id, link_type) -> ReturnDict:
    if link_type == Link.LinkType.EVENT:
        try:
            event = Event.objects.get(id=link_id)
            return EventSerializer(event).data
        except Event.DoesNotExist:
            return None

    elif link_type == Link.LinkType.RESOURCE:
        try:
            resource = Resource.objects.get(id=link_id)
            return ResourceSerializer(resource).data
        except Resource.DoesNotExist:
            return None

    elif link_type == Link.LinkType.CLIP:
        try:
            clip = Clip.objects.get(id=link_id)
            return ClipDetailSerializer(clip).data
        except Clip.DoesNotExist:
            return None

    else:
        return None


def get_links_for_id_and_type(link_id, link_type) -> QuerySet:
    if link_type == Link.LinkType.EVENT.value:
        min_event = Link.objects.filter(min_link_event_id=link_id).exclude(max_link_event_id=link_id)
        max_event = Link.objects.filter(max_link_event_id=link_id).exclude(max_link_event_id=link_id)
        return min_event | max_event
    elif link_type == Link.LinkType.RESOURCE.value:
        min_resource = Link.objects.filter(min_link_resource_id=link_id).exclude(max_link_resource_id=link_id)
        max_resource = Link.objects.filter(max_link_resource_id=link_id).exclude(min_link_resource_id=link_id)
        resources = min_resource | max_resource
        clip_ids = [c.id for c in Clip.objects.filter(resource_id=link_id)]
        clips = [get_links_for_id_and_type(cid, Link.LinkType.CLIP.value) for cid in clip_ids]
        clip_links = reduce(lambda a, b: a | b, clips, Link.objects.none())
        return resources | clip_links
    elif link_type == Link.LinkType.CLIP.value:
        min_clip = Link.objects.filter(min_link_clip_id=link_id).exclude(max_link_clip_id=link_id)
        max_clip = Link.objects.filter(max_link_clip_id=link_id).exclude(min_link_clip_id=link_id)
        return min_clip | max_clip
    return Link.objects.none()


def get_link_count(link_id, link_type) -> int:
    return len(get_links_for_id_and_type(link_id, link_type))

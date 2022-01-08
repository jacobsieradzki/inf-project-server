from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from classroomapi.models import Link, Event, Resource, Clip
from .event import EventSerializer
from .resource import ResourceSerializer
from .clip import ClipSerializer


def get_link_object(link_id, link_type):
    if link_type == "EVENT":
        try:
            event = Event.objects.get(id=link_id)
            return EventSerializer(event).data
        except Event.DoesNotExist:
            return None

    elif link_type == "RESOURCE":
        try:
            resource = Resource.objects.get(id=link_id)
            return ResourceSerializer(resource).data
        except Resource.DoesNotExist:
            return None

    elif link_type == "CLIP":
        try:
            clip = Clip.objects.get(id=link_id)
            return ClipSerializer(clip).data
        except Clip.DoesNotExist:
            return None

    else:
        return None


class LinkSerializer(HyperlinkedModelSerializer):
    min_link = SerializerMethodField()
    max_link = SerializerMethodField()

    class Meta:
        model = Link
        fields = ['id', 'course_id', 'anchor_id',
                  'min_link_type', 'min_link_id', 'min_link',
                  'max_link_type', 'max_link_id', 'max_link']

    def get_min_link(self, obj):
        return get_link_object(obj.min_link_id, obj.min_link_type)

    def get_max_link(self, obj):
        return get_link_object(obj.max_link_id, obj.max_link_type)

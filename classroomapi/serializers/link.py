from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from classroomapi.models import Link, Event, Resource, Clip
from .event import EventSerializer
from .resource import ResourceSerializer
from .clip import ClipSerializer


def get_link_object(link_id, link_type):
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
            return ClipSerializer(clip).data
        except Clip.DoesNotExist:
            return None

    else:
        return None


class LinkSerializer(HyperlinkedModelSerializer):
    min_link_type = SerializerMethodField(method_name="get_min_link_type")
    min_link_id = SerializerMethodField(method_name="get_min_link_id")
    min_link = SerializerMethodField(method_name="get_min_link")
    max_link_type = SerializerMethodField(method_name="get_max_link_type")
    max_link_id = SerializerMethodField(method_name="get_max_link_id")
    max_link = SerializerMethodField(method_name="get_max_link")

    class Meta:
        model = Link
        fields = ['id', 'course_id', 'subtitle_id',
                  'min_link_type', 'min_link_id', 'min_link',
                  'max_link_type', 'max_link_id', 'max_link']

    def get_min_link_type(self, obj: Link):
        return obj.get_min_type().value

    def get_min_link_id(self, obj: Link):
        return obj.get_min_id()

    def get_min_link(self, obj: Link):
        return get_link_object(obj.get_min_id(), obj.get_min_type())

    def get_max_link_type(self, obj: Link):
        return obj.get_max_type().value

    def get_max_link_id(self, obj: Link):
        return obj.get_max_id()

    def get_max_link(self, obj: Link):
        return get_link_object(obj.get_max_id(), obj.get_max_type())

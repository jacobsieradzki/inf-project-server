from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from classroomapi.models import Link, Event, Resource, Clip
from .event import EventSerializer
from .resource import ResourceSerializer
from .clip import ClipSerializer
from .link import get_link_object


# class LectureLinkSerializer:

    # class Subtitles(HyperlinkedModelSerializer):
    #
    #
    # class Links(HyperlinkedModelSerializer):
    #
    #
    # class OtherLinks(HyperlinkedModelSerializer):
    #     min_link = SerializerMethodField()
    #     max_link = SerializerMethodField()
    #
    #     class Meta:
    #         model = Link
    #         fields = ['id', 'course_id', 'anchor_id',
    #                   'min_link_type', 'min_link_id', 'min_link',
    #                   'max_link_type', 'max_link_id', 'max_link']
    #
    #     def get_min_link(self, obj):
    #         return get_link_object(obj.min_link_id, obj.min_link_type)
    #
    #     def get_max_link(self, obj):
    #         return get_link_object(obj.max_link_id, obj.max_link_type)

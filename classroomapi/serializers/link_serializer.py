from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from classroomapi.helper.links import get_link_object, get_link_count
from classroomapi.models import Link
from .subtitle_serializer import SubtitleSerializer
import json


class LinkSerializer(HyperlinkedModelSerializer):
    subtitle = SubtitleSerializer()
    min_link_type = SerializerMethodField()
    min_link_id = SerializerMethodField()
    min_link = SerializerMethodField()
    max_link_type = SerializerMethodField()
    max_link_id = SerializerMethodField()
    max_link = SerializerMethodField()

    class Meta:
        model = Link
        fields = ['id', 'course_id', 'subtitle',
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


class ShyLinkSerializer(HyperlinkedModelSerializer):
    link_type = SerializerMethodField()
    link_id = SerializerMethodField()
    link_other_count = SerializerMethodField()
    link = SerializerMethodField()
    source_link = SerializerMethodField()
    source_id = SerializerMethodField()

    class Meta:
        model = Link
        fields = ['id', 'course_id', 'subtitle_id', 'link_type', 'link_id', 'link_other_count', 'source_link', 'source_id', 'link']

    def get_link_type(self, obj: Link):
        if self.should_use_min(obj):
            return obj.get_min_type().value
        else:
            return obj.get_max_type().value

    def get_link_id(self, obj: Link):
        if self.should_use_min(obj):
            return obj.get_min_id()
        else:
            return obj.get_max_id()

    def get_link(self, obj: Link):
        return get_link_object(self.get_link_id(obj), self.get_link_type(obj))

    def get_link_other_count(self, obj: Link):
        return get_link_count(self.get_link_id(obj), self.get_link_type(obj))-1

    def get_source_id(self, obj: Link):
        linked_id = self.context.get('id')
        if obj.min_link_clip or obj.max_link_clip:
            return obj.max_link_clip.id if self.should_use_min(obj) else obj.min_link_clip.id
        else:
            return linked_id

    def get_source_link(self, obj: Link):
        if self.should_search_clips(obj):
            return get_link_object(self.get_source_id(obj), "CLIP")
        return None

    def should_use_min(self, obj: Link):
        linked_id = self.context.get('id')
        linked_type = self.context.get('type')
        if linked_id and linked_type:
            match_resource_id = not (obj.get_min_type().value == linked_type and str(obj.get_min_id()) == str(linked_id))
            if obj.min_link_clip or obj.max_link_clip:
                match_clip_id = not (str(obj.min_link_clip.resource_id) == str(linked_id))
                return match_resource_id and match_clip_id
            else:
                return match_resource_id
        else:
            return True

    def should_search_clips(self, obj: Link):
        return obj.min_link_clip or obj.max_link_clip

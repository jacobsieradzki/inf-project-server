from rest_framework.serializers import HyperlinkedModelSerializer, SerializerMethodField
from classroomapi.models import Link
from classroomapi.helper.links import get_link_object, get_link_count
from .subtitle_serializer import SubtitleSerializer


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

    class Meta:
        model = Link
        fields = ['id', 'course_id', 'subtitle_id', 'link_type', 'link_id', 'link_other_count', 'link']

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

    def should_use_min(self, obj: Link):
        linked_id = self.context.get('id')
        linked_type = self.context.get('type')
        if linked_id and linked_type:
            return obj.get_min_type().value == linked_type and obj.get_min_id() == linked_id
        else:
            return True

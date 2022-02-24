from rest_framework.serializers import HyperlinkedModelSerializer
from classroomapi.models import Clip, Highlight, HighlightRect
from . import ResourceSerializer, HighlightSerializer


def _create_highlight_from_data(data, resource_id) -> Highlight:
    highlight = Highlight()
    highlight.id = data.get('id')
    highlight.resource_id = resource_id

    bounding_rect = _create_rect_from_data(data.get('bounding_rect'))
    bounding_rect.save()
    highlight.bounding_rect = bounding_rect
    highlight.save()

    for rect_data in data.get('rects'):
        rect = _create_rect_from_data(rect_data)
        rect.parent = highlight
        rect.save()

    return highlight


def _create_rect_from_data(data) -> HighlightRect:
    rect = HighlightRect()
    rect.x1 = data.get('x1')
    rect.x2 = data.get('x2')
    rect.y1 = data.get('y1')
    rect.y2 = data.get('y2')
    rect.width = data.get('width')
    rect.height = data.get('height')
    rect.page_number = data.get('page_number')
    return rect


class ClipSerializer(HyperlinkedModelSerializer):
    highlight = HighlightSerializer()

    class Meta:
        model = Clip
        fields = ['id', 'course_id', 'resource_id', 'content', 'description', 'emoji', 'type',
                  'start_location', 'end_location', 'highlight', 'created_at', 'updated_at']

    def create(self, validated_data):
        rid = self.initial_data.get('resource_id')

        clip = Clip()
        clip.course_id = self.initial_data.get('course_id')
        clip.resource_id = rid
        clip.content = validated_data.get('content')
        clip.description = validated_data.get('description')
        clip.emoji = validated_data.get('emoji')
        clip.type = validated_data.get('type')
        clip.start_location = validated_data.get('start_location')
        clip.end_location = validated_data.get('end_location')
        clip.highlight = _create_highlight_from_data(self.initial_data.get('highlight'), rid)
        clip.save()
        return clip


class ClipDetailSerializer(HyperlinkedModelSerializer):
    resource = ResourceSerializer()
    highlight = HighlightSerializer()

    class Meta:
        model = Clip
        fields = ['id', 'course_id', 'resource', 'content', 'description', 'type',
                  'start_location', 'end_location', 'highlight', 'created_at', 'updated_at']

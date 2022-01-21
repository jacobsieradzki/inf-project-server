from rest_framework.serializers import HyperlinkedModelSerializer
from classroomapi.models import Highlight, HighlightRect


class HighlightRectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = HighlightRect
        fields = ['x1', 'x2', 'y1', 'y2', 'width', 'height', 'page_number']


class HighlightSerializer(HyperlinkedModelSerializer):
    bounding_rect = HighlightRectSerializer()
    rects = HighlightRectSerializer(read_only=True, many=True, source='highlightrect.parent')

    class Meta:
        model = Highlight
        fields = ['id', 'course_id', 'resource_id', 'title', 'emoji', 'content', 'type', 'bounding_rect', 'rects', 'created_at', 'updated_at']


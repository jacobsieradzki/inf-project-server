from rest_framework.serializers import HyperlinkedModelSerializer
from classroomapi.models import Clip
from . import ResourceSerializer, HighlightSerializer


class ClipSerializer(HyperlinkedModelSerializer):
    highlight = HighlightSerializer()

    class Meta:
        model = Clip
        fields = ['id', 'course_id', 'resource_id', 'content', 'description', 'type', 'start_location', 'end_location', 'highlight']


class ClipDetailSerializer(HyperlinkedModelSerializer):
    resource = ResourceSerializer()
    highlight = HighlightSerializer()

    class Meta:
        model = Clip
        fields = ['id', 'course_id', 'resource', 'content', 'description', 'type', 'start_location', 'end_location', 'highlight']

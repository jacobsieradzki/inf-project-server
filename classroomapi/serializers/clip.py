from rest_framework.serializers import HyperlinkedModelSerializer
from classroomapi.serializers import ResourceSerializer
from classroomapi.models import Clip


class ClipSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Clip
        fields = ['id', 'course_id', 'resource_id', 'content', 'description', 'type', 'start_location', 'end_location']


class ClipDetailSerializer(HyperlinkedModelSerializer):
    resource = ResourceSerializer()

    class Meta:
        model = Clip
        fields = ['id', 'course_id', 'resource', 'content', 'description', 'type', 'start_location', 'end_location']

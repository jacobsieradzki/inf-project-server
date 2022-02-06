from rest_framework.serializers import HyperlinkedModelSerializer
from classroomapi.models import Resource, Event
from .course_serializer import CourseSerializer


class ResourceSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'course_id', 'name', 'description', 'type', 'url', 'status']


class _SingleResourceEventSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'course_id', 'name', 'description', 'type', 'start_date', 'end_date']


class SingleResourceSerializer(HyperlinkedModelSerializer):
    course = CourseSerializer()
    parent_events = _SingleResourceEventSerializer(read_only=True, many=True, source='event_set')

    class Meta:
        model = Resource
        fields = ['id', 'course', 'name', 'description', 'type', 'url', 'status', 'parent_events']

from rest_framework.serializers import HyperlinkedModelSerializer
from classroomapi.models import Event
from .course_serializer import CourseSerializer
from .resource_serializer import ResourceSerializer


class EventSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'course_id', 'primary_resource_id', 'name', 'description', 'type', 'start_date', 'end_date']


class EventDetailSerializer(HyperlinkedModelSerializer):
    course = CourseSerializer()
    primary_resource = ResourceSerializer()

    class Meta:
        model = Event
        fields = ['id', 'course', 'primary_resource', 'name', 'description', 'type', 'start_date', 'end_date']

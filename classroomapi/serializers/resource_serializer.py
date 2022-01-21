from rest_framework.serializers import HyperlinkedModelSerializer
from classroomapi.models import Resource
from classroomapi.serializers import CourseSerializer


class ResourceSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'course_id', 'name', 'description', 'type', 'url', 'status']


class SingleResourceSerializer(HyperlinkedModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Resource
        fields = ['id', 'course', 'name', 'description', 'type', 'url', 'status']

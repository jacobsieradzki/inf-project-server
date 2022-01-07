from rest_framework.serializers import HyperlinkedModelSerializer
from classroomapi.models import Resource


class ResourceSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'course_id', 'name', 'description', 'type', 'url']
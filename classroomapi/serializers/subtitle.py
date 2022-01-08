from rest_framework.serializers import HyperlinkedModelSerializer
from classroomapi.models import Subtitle


class SubtitleSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Subtitle
        fields = ['id', 'course_id',  'resource_id',  'content',  'start_seconds']

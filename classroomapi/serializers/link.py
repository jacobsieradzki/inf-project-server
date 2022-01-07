from rest_framework.serializers import HyperlinkedModelSerializer
from classroomapi.models import Link


class LinkSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'min_course',  'min_link_id',  'min_link_type',  'max_course',  'max_link_id',  'max_link_type']

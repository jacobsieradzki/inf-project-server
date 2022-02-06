from rest_framework.serializers import HyperlinkedModelSerializer
from classroomapi.models import Course
from .organisation_serializer import OrganisationSerializer


class CourseSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'organisation_id', 'name', 'start_date', 'end_date']


class CourseDetailSerializer(HyperlinkedModelSerializer):
    organisation = OrganisationSerializer()

    class Meta:
        model = Course
        fields = ['id', 'organisation', 'name', 'start_date', 'end_date']

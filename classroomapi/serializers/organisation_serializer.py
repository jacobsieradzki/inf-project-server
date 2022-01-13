from rest_framework.serializers import HyperlinkedModelSerializer
from classroomapi.models import Organisation


class OrganisationSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Organisation
        fields = ['id', 'name', 'image_url']

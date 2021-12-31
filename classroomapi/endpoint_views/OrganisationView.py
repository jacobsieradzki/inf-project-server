from rest_framework import views
from classroomapi.models import Organisation
from classroomapi.serializers import OrganisationSerializer
from . import EndpointResponse


class OrganisationView(views.APIView):
    """
    Get all organisations, or organisation by id
    """
    def get(self, request, organisation_id=None):
        if organisation_id is not None:
            try:
                organisation = Organisation.objects.get(id=organisation_id)
                serializer = OrganisationSerializer(organisation)
                return EndpointResponse.success(data=serializer.data)
            except Organisation.DoesNotExist:
                return EndpointResponse.not_found("Organisation not found")

        else:
            organisations = Organisation.objects.all()
            serializer = OrganisationSerializer(organisations, many=True)
            return EndpointResponse.success(data=serializer.data)

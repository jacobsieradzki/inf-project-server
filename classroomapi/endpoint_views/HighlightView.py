from rest_framework import views
from classroomapi.serializers import HighlightSerializer
from classroomapi.models import Highlight
from . import EndpointResponse


class HighlightView(views.APIView):
    """
    Get all highlights for a resource
    """
    def get(self, request, resource_id):
        highlights = Highlight.objects.filter(resource_id=resource_id)
        serializer = HighlightSerializer(highlights, many=True)
        return EndpointResponse.success(data=serializer.data)

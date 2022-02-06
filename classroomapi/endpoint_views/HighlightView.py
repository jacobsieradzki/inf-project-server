from rest_framework import views
from classroomapi.serializers import HighlightSerializer
from classroomapi.models import Highlight
from . import EndpointResponse


class HighlightView(views.APIView):
    """
    Get all highlights for a resource
    """
    def get(self, request):
        highlights = Highlight.objects.all()
        serializer = HighlightSerializer(highlights, many=True)
        return EndpointResponse.success(data=serializer.data)

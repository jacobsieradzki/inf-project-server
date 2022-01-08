from rest_framework import views
from classroomapi.models import Clip
from classroomapi.serializers import ClipSerializer
from . import EndpointResponse


class ClipView(views.APIView):
    """
    Get all clips for a course, or by linked_id
    """
    def get(self, request, course_id):
        resource_id = request.query_params.get("resource_id")

        if resource_id is not None:
            clips = Clip.objects.filter(resource_id=resource_id)
            serializer = ClipSerializer(clips, many=True)
            return EndpointResponse.success(data=serializer.data)

        else:
            clips = Clip.objects.filter(course_id=course_id)
            serializer = ClipSerializer(clips, many=True)
            return EndpointResponse.success(data=serializer.data)

from rest_framework import views
from classroomapi.models import Subtitle
from classroomapi.serializers import SubtitleSerializer
from . import EndpointResponse


class SubtitleView(views.APIView):
    """
    Get all subtitles for a video
    """
    def get(self, request, course_id, resource_id):
        subtitles = Subtitle.objects.filter(course_id=course_id, resource_id=resource_id)
        serializer = SubtitleSerializer(subtitles, many=True)
        return EndpointResponse.success(data=serializer.data)

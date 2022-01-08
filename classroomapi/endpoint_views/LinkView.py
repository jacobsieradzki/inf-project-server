from rest_framework import views
from classroomapi.models import Link
from classroomapi.serializers import LinkSerializer
from . import EndpointResponse


class LinkView(views.APIView):
    """
    Get all links for a course, or by linked_id
    """
    def get(self, request):
        course_id = request.query_params.get("course_id")
        linked_id = request.query_params.get("linked_id")

        if course_id is not None:
            links = Link.objects.filter(course_id=course_id)
            serializer = LinkSerializer(links, many=True)
            return EndpointResponse.success(data=serializer.data)

        elif linked_id is not None:
            min_link_id_matches = Link.objects.filter(min_link_id=linked_id)
            max_link_id_matches = Link.objects.filter(max_link_id=linked_id)
            links = min_link_id_matches + max_link_id_matches
            serializer = LinkSerializer(links, many=True)
            return EndpointResponse.success(data=serializer.data)

        else:
            return EndpointResponse.bad_request(debug_message="Missing course_id or linked_id parameters")

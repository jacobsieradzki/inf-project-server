from rest_framework import views
from classroomapi.models import Link
from classroomapi.serializers import LinkSerializer
from . import EndpointResponse


class LinkView(views.APIView):
    """
    Get all links for a course, or by linked_id
    """
    def get(self, request, course_id):
        linked_id = request.query_params.get("id")
        linked_type = request.query_params.get("type")

        if (linked_id is not None and linked_type is None) or (linked_id is None and linked_type is not None):
            return EndpointResponse.bad_request(debug_message="Must provide id and type")

        if linked_id is not None:
            min_link_id_matches = Link.objects.filter(min_link_id=linked_id, min_link_type=linked_type)
            max_link_id_matches = Link.objects.filter(max_link_id=linked_id, max_link_type=linked_type)
            links = min_link_id_matches | max_link_id_matches
            serializer = LinkSerializer(links, many=True)
            return EndpointResponse.success(data=serializer.data)

        else:
            links = Link.objects.filter(course_id=course_id)
            serializer = LinkSerializer(links, many=True)
            return EndpointResponse.success(data=serializer.data)

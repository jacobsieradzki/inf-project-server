from rest_framework import views
from classroomapi.models import Link
from classroomapi.serializers import ShyLinkSerializer, LinkSerializer
from classroomapi.helper.links import get_links_for_id_and_type
from . import EndpointResponse


class LinkView(views.APIView):
    """
    Get all links for a course, or by linked_id
    """

    def get(self, request, course_id):
        linked_id = request.query_params.get("id")
        linked_type = request.query_params.get("type")

        if bool(linked_id) != bool(linked_type):
            return EndpointResponse.bad_request(debug_message="Must provide id and type")

        elif linked_id and linked_type:
            links = get_links_for_id_and_type(linked_id, linked_type)
            serializer = ShyLinkSerializer(links, many=True)
            return EndpointResponse.success(data=serializer.data)

        else:
            links = Link.objects.filter(course_id=course_id)
            serializer = LinkSerializer(links, many=True)
            return EndpointResponse.success(data=serializer.data)

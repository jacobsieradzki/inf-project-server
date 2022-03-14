from rest_framework import views
from classroomapi.models import Link
from classroomapi.serializers import ShyLinkSerializer, LinkSerializer
from classroomapi.helper.links import get_links_for_id_and_type, create_link
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
            serializer = ShyLinkSerializer(links, many=True, context={'id': linked_id, 'type': linked_type})
            return EndpointResponse.success(data=serializer.data)

        else:
            links = Link.objects.filter(course_id=course_id)
            serializer = LinkSerializer(links, many=True)
            return EndpointResponse.success(data=serializer.data)

    def post(self, request, course_id):
        subtitle_id = request.data.get('subtitle_id', '')
        from_id = str(request.data.get('from_id'))
        from_type = request.data.get('from_type')
        to_id = str(request.data.get('to_id'))
        to_type = request.data.get('to_type')

        link = create_link(course_id, subtitle_id, from_id, from_type, to_id, to_type)
        link.save()

        serializer = LinkSerializer(link)
        return EndpointResponse.success_created(data=serializer.data)


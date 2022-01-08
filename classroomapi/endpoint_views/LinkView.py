from rest_framework import views
from classroomapi.models import Link
from classroomapi.serializers import LinkSerializer
from . import EndpointResponse


def get_links_for_id_and_type(linked_id, linked_type):
    if linked_type == Link.LinkType.EVENT.value:
        min_event = Link.objects.filter(min_link_event_id=linked_id)
        max_event = Link.objects.filter(max_link_event_id=linked_id)
        return min_event | max_event
    elif linked_type == Link.LinkType.RESOURCE.value:
        min_resource = Link.objects.filter(min_link_resource_id=linked_id)
        max_resource = Link.objects.filter(max_link_resource_id=linked_id)
        return min_resource | max_resource
    elif linked_type == Link.LinkType.CLIP.value:
        min_clip = Link.objects.filter(min_link_clip_id=linked_id)
        max_clip = Link.objects.filter(max_link_clip_id=linked_id)
        return min_clip | max_clip
    return Link.objects.none()


class LinkView(views.APIView):
    """
    Get all links for a course, or by linked_id
    """

    def get(self, request, course_id):
        linked_id = request.query_params.get("id")
        linked_type = request.query_params.get("type")

        if not (linked_id and linked_type):
            return EndpointResponse.bad_request(debug_message="Must provide id and type")

        if linked_id is not None:
            links = get_links_for_id_and_type(linked_id, linked_type)
            serializer = LinkSerializer(links, many=True)
            return EndpointResponse.success(data=serializer.data)

        else:
            links = Link.objects.filter(course_id=course_id)
            serializer = LinkSerializer(links, many=True)
            return EndpointResponse.success(data=serializer.data)

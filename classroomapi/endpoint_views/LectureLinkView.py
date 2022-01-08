from rest_framework import views
from classroomapi.models import Event, Subtitle
from classroomapi.serializers import SubtitleSerializer
from .LinkView import get_links_for_id_and_type
from . import EndpointResponse


def get_event(course_id, event_id):
    try:
        event = Event.objects.get(id=event_id, course_id=course_id)
        return event
    except Event.DoesNotExist:
        return None


class LectureLinkView(views.APIView):
    """
    `/link/{course_id}/lecture/{event_id}`

    Get all links for a lecture video: split into subtitles, links, other_links
    """
    def get(self, request, course_id, event_id):
        event = get_event(course_id, event_id)
        if event is None:
            return EndpointResponse.not_found(message="Event not found")
        if event.type != Event.EventType.LECTURE.value:
            return EndpointResponse.bad_request(debug_message="Event is not a lecture")
        if event.primary_resource is None:
            return EndpointResponse.bad_request(message="Event does not have a primary_resource")

        subtitles = Subtitle.objects.filter(course_id=course_id, resource_id=event.primary_resource.id)
        subtitle_serializer = SubtitleSerializer(subtitles, many=True)

        output = {
            "subtitles": subtitle_serializer.data
        }

        return EndpointResponse.success(output)

        # event_links = get_links_for_id_and_type(event.id, "EVENT")
        # primary_resource_links = get_links_for_id_and_type(event.primary_resource.id, "RESOURCE")
        # links = event_links | primary_resource_links
        #
        # serializer = LinkSerializer(links, many=True)
        # return EndpointResponse.success(data=serializer.data)

        # if (linked_id is not None and linked_type is None) or (linked_id is None and linked_type is not None):
        #     return EndpointResponse.bad_request(debug_message="Must provide id and type")
        #
        # if linked_id is not None:
        #     min_link_id_matches = Link.objects.filter(min_link_id=linked_id, min_link_type=linked_type)
        #     max_link_id_matches = Link.objects.filter(max_link_id=linked_id, max_link_type=linked_type)
        #     links = min_link_id_matches | max_link_id_matches
        #     serializer = LinkSerializer(links, many=True)
        #     return EndpointResponse.success(data=serializer.data)
        #
        # else:
        #     links = Link.objects.filter(course_id=course_id)
        #     serializer = LinkSerializer(links, many=True)
        #     return EndpointResponse.success(data=serializer.data)


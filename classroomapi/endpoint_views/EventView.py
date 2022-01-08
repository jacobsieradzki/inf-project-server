from rest_framework import views
from classroomapi.models import Event
from classroomapi.serializers import EventSerializer, EventDetailSerializer
from . import EndpointResponse


class EventView(views.APIView):
    """
    Get all events, or event by id
    """
    def get(self, request, course_id, event_id=None):
        if event_id is not None:
            try:
                event = Event.objects.get(id=event_id, course_id=course_id)
                serializer = EventDetailSerializer(event)
                return EndpointResponse.success(data=serializer.data)
            except Event.DoesNotExist:
                return EndpointResponse.not_found("Event not found")

        else:
            events = Event.objects.filter(course_id=course_id)
            serializer = EventSerializer(events, many=True)
            return EndpointResponse.success(data=serializer.data)

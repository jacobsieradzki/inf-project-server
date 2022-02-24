from rest_framework import views
from classroomapi.serializers import HighlightSerializer, ClipSerializer
from classroomapi.models import Result, Highlight
from . import EndpointResponse
from classroomapi.helper import permissions


def get_clip_from_data(data):
    serializer = ClipSerializer(data=data)
    if serializer.is_valid():
        return Result(data=serializer)
    else:
        return Result(error=str(serializer.errors))


class HighlightView(views.APIView):

    def get(self, request, resource_id):
        highlights = Highlight.objects.filter(resource_id=resource_id)
        serializer = HighlightSerializer(highlights, many=True)
        return EndpointResponse.success(data=serializer.data)

    def post(self, request, resource_id):
        p1 = permissions.has_student_membership_to_resource(request.user, resource_id)
        p2 = permissions.has_staff_membership_to_resource(request.user, resource_id)

        if p1.is_error:
            return EndpointResponse.unauthorized(message=p1.error)
        if p2.is_error:
            return EndpointResponse.unauthorized(message=p2.error)

        new_clip = get_clip_from_data(request.data)
        if new_clip.is_success:
            serializer: ClipSerializer = new_clip.data
            serializer.save()
            return EndpointResponse.success_created(serializer.data)
        else:
            return EndpointResponse.success(data={
                'errors': new_clip.error
            })


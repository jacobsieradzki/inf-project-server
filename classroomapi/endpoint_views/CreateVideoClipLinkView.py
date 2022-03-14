from rest_framework import views
from classroomapi.models import Clip
from classroomapi.serializers import LinkSerializer
from classroomapi.helper.links import create_link
from . import EndpointResponse


class CreateVideoClipLinkView(views.APIView):
    """
    Create video clip -> create link
    """
    def post(self, request):
        course_id = request.data.get('course_id')
        subtitle_id = request.data.get('subtitle_id')
        from_id = request.data.get('from_id')
        from_type = request.data.get('from_type')
        video_id = request.data.get('video_id')
        content_param = request.data.get('content', '')
        description_param = request.data.get('description', '')
        start_location = request.data.get('start_location', 0)
        end_location = request.data.get('end_location', 0)

        if not (course_id and video_id and from_id and from_type):
            return EndpointResponse.bad_request(debug_message="Missing course_id, video_id, from_id or from_type")

        clip = Clip(course_id=course_id,
                    resource_id=video_id,
                    start_location=start_location,
                    end_location=end_location,
                    content=content_param,
                    description=description_param,
                    type=Clip.ClipType.VIDEO_CLIP)
        clip.save()

        link = create_link(course_id=course_id,
                           subtitle_id=subtitle_id,
                           from_id=str(from_id),
                           from_type=from_type,
                           to_id=str(clip.id),
                           to_type="CLIP")
        link.save()

        serializer = LinkSerializer(link)
        return EndpointResponse.success_created(data=serializer.data)

from rest_framework import views
from classroomapi.models import Resource
from classroomapi.serializers import ResourceSerializer
from . import EndpointResponse
from classroomapi.helper import s3, transcribe


class CreatePDFHighlightView(views.APIView):
    """
    Create highlight on PDF -> creates Clip, Highlight & HighlightRect(s) objects
    """
    def post(self, request, course_id):
        name_param = request.data.get('name')
        description_param = request.data.get('description')
        type_param = request.data.get('type')
        url_param = request.data.get('url')
        file_obj = request.data.get('file')

        if not (name_param and type_param):
            return EndpointResponse.bad_request(debug_message="Missing parameters (required: name, type)")

        if not url_param and not file_obj:
            return EndpointResponse.bad_request(debug_message="Must provide url or file")

        if type_param == Resource.ResourceType.VID.value and not file_obj:
            return EndpointResponse.bad_request(debug_message="Must include file with VID resource")

        r = Resource(course_id=course_id,
                     name=name_param,
                     description=description_param or "",
                     type=type_param,
                     url=url_param or "",
                     status=Resource.StatusType.READY)
        r.save()

        # For lecture videos: upload to S3 and start transcription
        if type_param == Resource.ResourceType.VID.value and file_obj:
            upload_url, upload_error = s3.upload_video_resource(r.id, file_obj)
            if upload_error:
                r.status = Resource.StatusType.ERROR
            else:
                r.url = upload_url

                transcribe_response, transcribe_error = transcribe.start_video_resource_transcription(resource_id=r.id)
                if transcribe_error:
                    r.status = Resource.StatusType.ERROR
                else:
                    r.status = Resource.StatusType.PROCESSING
            r.save()

        serializer = ResourceSerializer(r)
        return EndpointResponse.success(data=serializer.data)

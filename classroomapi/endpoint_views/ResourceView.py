from rest_framework import views
from rest_framework.parsers import FormParser, MultiPartParser
from classroomapi.models import Resource
from classroomapi.serializers import ResourceSerializer, SingleResourceSerializer
from . import EndpointResponse
from classroomapi.helper import s3, transcribe


class ResourceView(views.APIView):
    """
    Get all resources, or resources by id
    """
    parser_classes = [FormParser, MultiPartParser]

    def get(self, request, course_id):
        resources = Resource.objects.filter(course_id=course_id).order_by('-updated_at')
        serializer = ResourceSerializer(resources, many=True)
        return EndpointResponse.success(data=serializer.data)

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


class SingleResourceView(views.APIView):
    """
    Get resource by id
    """

    def get(self, request, course_id, resource_id):
        try:
            resource = Resource.objects.get(id=resource_id, course_id=course_id)
            serializer = SingleResourceSerializer(resource)
            return EndpointResponse.success(data=serializer.data)
        except Resource.DoesNotExist:
            return EndpointResponse.not_found("Resource not found")

    def delete(self, request, course_id, resource_id):
        try:
            resource = Resource.objects.get(id=resource_id, course_id=course_id)
            resource.delete()
            return EndpointResponse.success()
        except Resource.DoesNotExist:
            return EndpointResponse.not_found("Resource not found")


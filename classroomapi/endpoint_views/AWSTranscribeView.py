from rest_framework import views
from django.db import transaction
from classroomapi.helper import transcribe, s3
from classroomapi.helper.datetime import parse_vtt_caption_to_seconds
from classroomapi.helper.objects import get_resource
from classroomapi.models import Subtitle, Resource
from classroomapi.serializers import SubtitleSerializer
from . import EndpointResponse
from io import StringIO
import webvtt


class AWSTranscribeView(views.APIView):

    def post(self, request):
        resource_id, job_status = transcribe.get_data_from_job_status_change(request.data)
        if not (resource_id and job_status):
            return EndpointResponse.bad_request(debug_message='Bad input: detail')

        resource = get_resource(resource_id)
        if not resource:
            return EndpointResponse.not_found(message='Resource not found')

        if job_status != "COMPLETED":
            resource.status = Resource.StatusType.ERROR
            resource.save()
            return EndpointResponse.success(data=[])

        vtt_contents = s3.get_object_text(transcribe.get_transcription_vtt_path(resource_id))
        if not vtt_contents:
            return EndpointResponse.not_found(message='Transcription not found')

        subtitles = []
        with transaction.atomic():
            for caption in webvtt.read_buffer(StringIO(vtt_contents)):
                s = Subtitle(course_id=resource.course_id,
                             resource_id=resource_id,
                             content=caption.text,
                             start_seconds=parse_vtt_caption_to_seconds(caption.start))
                s.save()
                subtitles.append(s)
            resource.status = Resource.StatusType.READY
            resource.save()

        serializer = SubtitleSerializer(subtitles, many=True)
        return EndpointResponse.success(data=serializer.data)



# {
#     "status": "success",
#     "data": {
#         "version": "0",
#         "id": "716ec160-afc3-9c77-0420-f5c52154c7f2",
#         "detail-type": "Transcribe Job State Change",
#         "source": "aws.transcribe",
#         "account": "005830418823",
#         "time": "2022-01-09T18:56:09Z",
#         "region": "eu-west-2",
#         "resources": [],
#         "detail": {
#             "TranscriptionJobName": "resource_22_22_01_09_17_55_12",
#             "TranscriptionJobStatus": "COMPLETED"
#         }
#     }
# }

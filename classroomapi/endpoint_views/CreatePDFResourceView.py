from rest_framework import views
from classroomapi.models import Resource, Clip
from classroomapi.serializers import ResourceSerializer
from . import EndpointResponse
from classroomapi.helper import s3, pdf


class CreatePDFResourceView(views.APIView):
    """
    Create highlight on PDF -> upload to s3, create Resource, create Clip for each page, then set READY status
    """
    def post(self, request):
        course_id = request.data.get('course_id')
        name_param = request.data.get('name', '')
        description_param = request.data.get('description', '')
        file_obj = request.data.get('file')

        if not len(course_id) > 0:
            return EndpointResponse.bad_request(debug_message="Must provide course id")
        if not len(name_param) > 0:
            return EndpointResponse.bad_request(debug_message="Must provide a name")
        if not file_obj:
            return EndpointResponse.bad_request(debug_message="Must provide PDF file")

        r = Resource(course_id=course_id,
                     name=name_param,
                     description=description_param or "",
                     type=Resource.ResourceType.PDF.value,
                     url="",
                     status=Resource.StatusType.PROCESSING)
        r.save()

        upload_url, upload_error = s3.upload_pdf_resource(r.id, file_obj)
        if upload_error:
            r.status = Resource.StatusType.ERROR
            r.save()
            serializer = ResourceSerializer(r)
            return EndpointResponse.server_error(debug_message="S3 upload failed", data={
                'upload_error': upload_error,
                'resource': serializer.data
            })

        r.url = upload_url
        r.save()

        images_result = pdf.get_images_from_pdf(upload_url)
        if images_result.is_error:
            r.status = Resource.StatusType.ERROR
            r.save()
            serializer = ResourceSerializer(r)
            return EndpointResponse.server_error(debug_message="PDF get images failed", data={
                'pdf_error': images_result.error,
                'resource': serializer.data
            })

        for idx, val in enumerate(images_result.data):
            c = Clip(course_id=course_id,
                     resource_id=r.id,
                     content=pdf.get_image_from_pdfimgdata(val),
                     description='',
                     type=Clip.ClipType.PDF_PAGE.value,
                     start_location=idx+1,
                     end_location=idx+1)
            c.save()

        r.status = Resource.StatusType.READY
        serializer = ResourceSerializer(r)
        return EndpointResponse.success(data=serializer.data)

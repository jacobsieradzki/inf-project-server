from rest_framework import views
from classroomapi.models import Resource, Link
from classroomapi.serializers import LinkSerializer
from classroomapi.helper.links import create_link
from . import EndpointResponse
from bs4 import BeautifulSoup
import tldextract
import requests


class CreateUrlLinkView(views.APIView):
    """
    Create video clip -> create link
    """

    def post(self, request):
        course_id = request.data.get('course_id')
        subtitle_id = request.data.get('subtitle_id')
        from_id = request.data.get('from_id')
        from_type = request.data.get('from_type')
        url_param = request.data.get('url')
        type_param = request.data.get('type', Resource.ResourceType.URL)
        name_param = request.data.get('name')
        description_param = request.data.get('description')

        if not (course_id and from_id and from_type and url_param):
            return EndpointResponse.bad_request(debug_message="Missing parameters")

        if not name_param:
            r = requests.get(url_param)
            soup = BeautifulSoup(r.text)
            name_param = soup.find("meta", property="og:title").get('content')

        if not description_param:
            description_param = tldextract.extract(url_param).fqdn

        resource = Resource(course_id=course_id,
                            name=name_param[0:60],
                            description=description_param[0:60],
                            url=url_param,
                            type=type_param,
                            status=Resource.StatusType.READY)
        resource.save()

        link = create_link(course_id=course_id,
                           subtitle_id=subtitle_id,
                           from_id=str(from_id),
                           from_type=from_type,
                           to_id=str(resource.id),
                           to_type="RESOURCE")
        link.save()

        serializer = LinkSerializer(link)
        return EndpointResponse.success_created(data=serializer.data)

from rest_framework import views
from classroomapi.models import Resource
from classroomapi.serializers import ResourceSerializer
from . import EndpointResponse


class ResourceView(views.APIView):
    """
    Get all resources, or resources by id
    """
    def get(self, request, course_id, resource_id=None):
        if resource_id is not None:
            try:
                resource = Resource.objects.get(id=resource_id, course_id=course_id)
                serializer = ResourceSerializer(resource)
                return EndpointResponse.success(data=serializer.data)
            except Resource.DoesNotExist:
                return EndpointResponse.not_found("Resource not found")

        else:
            resources = Resource.objects.filter(course_id=course_id)
            serializer = ResourceSerializer(resources, many=True)
            return EndpointResponse.success(data=serializer.data)

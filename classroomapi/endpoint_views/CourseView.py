from rest_framework import views
from classroomapi.serializers import CourseSerializer, CourseDetailSerializer
from classroomapi.models import Course
from . import EndpointResponse


class CourseView(views.APIView):
    """
    Get all courses
    """
    def get(self, request, course_id=None):
        if course_id is not None:
            try:
                course = Course.objects.get(id=course_id)
                serializer = CourseDetailSerializer(course)
                return EndpointResponse.success(data=serializer.data)
            except Course.DoesNotExist:
                return EndpointResponse.not_found("Course not found")

        else:
            organisation_id = request.query_params.get("organisation_id")
            if organisation_id is not None:
                courses = Course.objects.filter(organisation_id=organisation_id)
            else:
                courses = Course.objects.all()

            serializer = CourseSerializer(courses, many=True)
            return EndpointResponse.success(data=serializer.data)

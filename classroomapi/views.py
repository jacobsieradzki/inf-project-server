from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from classroomapi.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


# class OrganisationViewSet(viewsets.ModelViewSet):
#     queryset = models.Organisation.objects.all()
#     serializer_class = serializers.OrganisationSerializer
#
#
# class CourseViewSet(viewsets.ModelViewSet):
#     queryset = models.Course.objects.all()
#     serializer_class = serializers.CourseSerializer
#
#
# class EventViewSet(viewsets.ModelViewSet):
#     queryset = models.Event.objects.all()
#     serializer_class = serializers.EventSerializer
#
#
# class MeetingViewSet(viewsets.ModelViewSet):
#     queryset = models.Meeting.objects.all()
#     serializer_class = serializers.MeetingSerializer
#
#
# class ResourceViewSet(viewsets.ModelViewSet):
#     queryset = models.Resource.objects.all()
#     serializer_class = serializers.ResourceSerializer

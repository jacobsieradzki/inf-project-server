from django.contrib.auth.models import User, Group
from rest_framework import serializers
from classroomapi import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class OrganisationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Organisation
        fields = ['id', 'name']


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Course
        fields = ['id', 'organisation_id', 'name', 'start_date', 'end_date']


class MeetingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Meeting
        fields = ['id', 'course_id', 'name', 'description', 'url']


class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Resource
        fields = ['id', 'course_id', 'name', 'description', 'name', 'type', 'url']


class EventSerializer(serializers.HyperlinkedModelSerializer):
    course = CourseSerializer()
    primary_resource = ResourceSerializer()

    class Meta:
        model = models.Event
        fields = ['id', 'course', 'primary_resource', 'name', 'description', 'type', 'start_date', 'end_date']
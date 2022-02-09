from rest_framework.serializers import HyperlinkedModelSerializer
from classroomapi.models import Membership


class MembershipSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Membership
        fields = ['id', 'organisation_id', 'course_id', 'user_id', 'role', 'created_at', 'updated_at']

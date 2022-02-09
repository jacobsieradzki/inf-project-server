from rest_framework import views
from classroomapi.models import Membership
from classroomapi.serializers import MembershipSerializer
from . import EndpointResponse


class MembershipView(views.APIView):

    def get(self, request):
        user_data = request.user
        if not user_data:
            return EndpointResponse.unauthorized()

        memberships = Membership.objects.filter(user=user_data)
        serializer = MembershipSerializer(memberships, many=True, context={'request': request})
        return EndpointResponse.success(data=serializer.data)

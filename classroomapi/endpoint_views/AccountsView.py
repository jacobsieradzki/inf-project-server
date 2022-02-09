from rest_framework import views
from django.contrib.auth.models import User
from classroomapi.serializers import UserSerializer
from . import EndpointResponse


class AccountsView(views.APIView):
    def get(self, request):
        user_data = request.user
        if user_data:
            serializer = UserSerializer(user_data, context={'request': request})
            return EndpointResponse.success_created(data=serializer.data)
        else:
            return EndpointResponse.unauthorized()

    def post(self, request):
        serializer = UserSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = User.objects.create(
                username=request.data['username'],
                email=request.data['email'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name']
            )
            user.set_password(request.data['password'])
            user.save()
            serializer = UserSerializer(user, context={'request': request})
            return EndpointResponse.success_created(data=serializer.data)
        else:
            return EndpointResponse.bad_request(data=serializer.errors)

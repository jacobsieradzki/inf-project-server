from rest_framework import views
from rest_framework.response import Response

class HistoryView(views.APIView):

    def get(self, request):
        user = request.query_params["user"]

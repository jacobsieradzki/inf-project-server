from rest_framework import status
from rest_framework.response import Response


def success(data):
    return Response({
        "status": "success",
        "data": data
    }, status=status.HTTP_200_OK)


def error(message, status_id="error", data=None, error_status=status.HTTP_400_BAD_REQUEST):
    return Response({
        "status": status_id,
        "message": message,
        "data": data
    }, status=error_status)


def not_found(message="Item not found", data=None):
    return error(message,
                 status_id="not_found",
                 data=data,
                 error_status=status.HTTP_404_NOT_FOUND)


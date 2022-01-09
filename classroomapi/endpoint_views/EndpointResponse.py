from rest_framework import status
from rest_framework.response import Response


def success(data):
    return Response({
        "status": "success",
        "data": data
    }, status=status.HTTP_200_OK)


def error(message, debug_message=None, status_id="error", data=None, error_status=status.HTTP_400_BAD_REQUEST):
    return Response({
        "status": status_id,
        "message": message,
        "debug_message": debug_message,
        "data": data
    }, status=error_status)


def bad_request(message="Something went wrong with the request", debug_message="Bad request", data=None):
    return error(message=message,
                 debug_message=debug_message,
                 status_id="bad_request",
                 data=data,
                 error_status=status.HTTP_400_BAD_REQUEST)


def server_error(message="Something went wrong - please try again later", debug_message="Internal server error", data=None):
    return error(message=message,
                 debug_message=debug_message,
                 status_id="server_error",
                 data=data,
                 error_status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def not_found(message="Item not found", data=None):
    return error(message,
                 status_id="not_found",
                 data=data,
                 error_status=status.HTTP_404_NOT_FOUND)


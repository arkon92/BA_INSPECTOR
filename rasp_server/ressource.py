import supervisor as sup
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def start_video_capture(request):
    try:
        supervisor = sup.Supervisor("0")
        supervisor.create_inspector("1")
        return Response(status=status.HTTP_200_OK)
    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def stop_video_capture(request):
    try:
        supervisor = sup.Supervisor("0")
        supervisor.kill_inspector()
        return Response(status=status.HTTP_200_OK)
    except Exception:
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

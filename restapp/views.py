from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# ---------------------------------------------------------------------
# Funtion based view 로 구현
# ---------------------------------------------------------------------

@api_view(['POST'])
def sa_webhook(request):
    result = [ "{'status' : 200}" ]

    print(request.query_params)

    if request.query_params["format"] == "json":
        return Response(result)

    return Response(result)
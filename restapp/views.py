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
    return Response(result)


from django.http import JsonResponse

@api_view(['POST'])
def dialogflow(request):
    r = {"speech":"고기없어요","displayText":"고기없어요","messages":{"type": 0,"speech": "요즘 이시간에는 고기없어요"},"data":{},"contextOut":[],"source":"example.com","followupEvent":{}}
    return JsonResponse(r)

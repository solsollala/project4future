from rest_framework.response import Response
from rest_framework.decorators import api_view

# ---------------------------------------------------------------------
# Funtion based view 로 구현
# ---------------------------------------------------------------------
@api_view(['POST'])
def sa_webhook(request):
    result = [ "{'status' : 200}" ]
    return Response(result)


# ---------------------------------------------------------------------
# 다이얼로그 플로우가 Fullfillment 처리를 위해 호출하는 Webhook API
# ---------------------------------------------------------------------

from django.http import JsonResponse
from app_logics.dialog_v1 import fullfillment_webhook as dm
import json

@api_view(['POST'])
def dialogflow(request):
    request_body = json.loads(request.stream.read().decode('utf-8'))
    return JsonResponse(dm.webhook(request_body))

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
from .dialog_v1 import dialogManager as dm

@api_view(['POST'])
def dialogflow(request):

    # try:
    #     with open('~/project4future/fullfill_request.json', 'w') as f:
    #         f.write(str(request.stream.read().decode('utf-8')))
    #         f.close()
    # except:
    #     pass

    request_body = conver2json(request.stream.read().decode('utf-8'))

    return JsonResponse(dm.dialog(request_body))


import json

def conver2json(content):
    if type(content) is dict:
        return content
    if type(content) is str:
        return json.loads(content)
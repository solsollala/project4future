import os.path
import sys
import json

INTENT_TIDETIME = "200-fishing-getTideTime - custom"
INTENT_FISH = "102-fishing-getFish"

def dialog(request):
    intent = request['result']["metadata"]["intentName"]
    parameters = request['result']['parameters']

    msg = ''
    if INTENT_TIDETIME in intent:
        msg = '오늘의 물때는 5물이네요. 오전3시-오후3시 수위가 가장 낮고, 오전9시-오후9시 수위가 가장 높습니다.'
    elif INTENT_FISH in intent:
        msg = '이른 아침에는 고등어,학꽁치같은 회유성 어종이 나타나고, 해가 질 무렵에는 우럭이 나온다고 하네요.'

    response = {"speech": msg, "displayText": msg,"messages": {"type": 0, "speech": msg}}
    return response


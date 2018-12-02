# -*- coding:utf8 -*-
# !/usr/bin/env python
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path
import sys
import json

try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai


CLIENT_ACCESS_TOKEN = '872aa41e69774da89d2252c77beca37c'
LANGUAGE = 'ko-KR'

# SESSION_ID 관리해야 할 듯
import uuid
SESSION_ID = uuid.uuid4().hex

# ---------------------------------------------------------------------
# 챗봇이 대화를 위해 호출하는 함수
# ---------------------------------------------------------------------

def chat(query):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

    request = ai.text_request()
    request.lang = LANGUAGE
    request.session_id = SESSION_ID
    request.query = query

    response = json.loads(request.getresponse().read())

    return response['result']['fulfillment']['speech']


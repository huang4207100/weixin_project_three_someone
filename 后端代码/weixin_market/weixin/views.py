import json
from django.shortcuts import render
from django.http import JsonResponse
from .config import CODE2SESSION
import requests
# Create your views here.


def user_login(request):
    get_data = json.loads(request.body)
    codeurl = CODE2SESSION.substitute({'CODE': get_data['js_code']})
    result = requests.get(codeurl)
    re_json = {
        "succ": True,
        "msg": "",
        "data": json.loads(result.text)
    }
    return JsonResponse(re_json)

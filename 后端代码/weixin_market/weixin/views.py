import json
from django.shortcuts import render
from django.http import JsonResponse
from .config import CODE2SESSION
from .models import Weixin_user
from .login_interface.login_operation import write_login_header, generate_header_value
import requests
from weixin_market.settings import *

# Create your views here.
logger = logging.getLogger("weixin.view")


def user_login(request):
    get_data = json.loads(request.body)
    codeurl = CODE2SESSION.substitute({'CODE': get_data['js_code']})
    result = json.loads(requests.get(codeurl).text)
    try:
        if Weixin_user.objects.filter(openid=result["openid"]):
            logger.error("已有用户")
        else:
            Weixin_user(openid=result["openid"]).save()
    except KeyError:
        logger.error(f'error code cant get openid')
        return JsonResponse({"succ": False, "msg": "get openid fault", "data": {}})
    header_info = generate_header_value(result["openid"])
    write_login_header(result["openid"], header_info)
    re_json = {"succ": True, "msg": "", "data": header_info}
    return JsonResponse(re_json)

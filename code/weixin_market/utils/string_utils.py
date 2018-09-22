def get_rsp_body(data={}, succ=True, code=0, msg=''):
    """
    返回结构体给客户端
    {
        'succ': #<bool> True or False, 调用是否成功
        "code": 0 #<int>  返回识别码, succ == False的情况返回的是error code
        "message": "操作成功" #<string>
        "data": { ... } #<json dict>
    }
    :return:
    """

    r = {
        'succ': bool(succ),
        'code': int(code),
        'message': str(msg),
    }

    if data is not None:
        r['data'] = data

    return r


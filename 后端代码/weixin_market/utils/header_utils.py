#生成登陆的header
def gen_user_sign_header(tenant_id, user_id):
    login_time = int(time.time())
    return {
        'UID': '%s' % (int(user_id)),
        'TENANTID': '%s' % (int(tenant_id)),
        'LTIME': '%s' % (login_time),
        'SIGN': convert_to_md5_str('%s_%s_%s_%s' % (user_id, tenant_id, login_time, URL_SIGN_CHECK_SECRET)),
    }

#将header写入到redis
def write_login_token(tenant_id, user_id, header_info):
    login_key = 'ADMIN_LOGIN_%s_%s' % (tenant_id, user_id)
    write_to_redis_hash(login_key, header_info)
    touch_login_token(tenant_id=tenant_id, user_id=user_id)


#将header的生命周期延长30分钟
def touch_login_token(tenant_id, user_id):
    login_key = 'ADMIN_LOGIN_%s_%s' % (tenant_id, user_id)
    get_redis_connection().expire(login_key, 6*60*60)  # 30分钟

#删除header
def del_login_token(tenant_id, user_id):
    login_key = 'ADMIN_LOGIN_%s_%s' % (tenant_id, user_id)
    del_from_redis(login_key)


#得到header
def get_login_token_from_cache(tenant_id, user_id):
    login_key = 'ADMIN_LOGIN_%s_%s' % (tenant_id, user_id)
    return read_from_redis_hash(login_key)
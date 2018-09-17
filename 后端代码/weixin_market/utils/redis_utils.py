import redis
from weixin_market.settings import REDIS_CONFIG
import json


pool = redis.ConnectionPool(
    host=REDIS_CONFIG["redis_ip"], port=REDIS_CONFIG["redis_port"], password=REDIS_CONFIG["redis_auth"], db=REDIS_CONFIG["redis_db"])


def get_redis_connection():
    return redis.Redis(connection_pool=pool)

# 延长 redis_key 生命
def prolong_redis_key(redis_key, seconds):
    """
    延长 redis_key 生命
    :param redis_key: 被延长的 key
    :param seconds: 要延长的时间(秒)
    :return:
    """
    get_redis_connection().expire(redis_key, seconds)

'''
删除一
'''
def del_from_redis(*keys):
    get_redis_connection().delete(*keys)


'''
写入单个值

"""
    Set the value at key ``name`` to ``value``

    ``ex`` sets an expire flag on key ``name`` for ``ex`` seconds.

    ``px`` sets an expire flag on key ``name`` for ``px`` milliseconds.

    ``nx`` if set to True, set the value at key ``name`` to ``value`` only
        if it does not exist.

    ``xx`` if set to True, set the value at key ``name`` to ``value`` only
        if it already exists.
"""
:return true for write ok, else is fail

'''
def write_to_redis(key, value, ex=None, px=None, nx=False, xx=False):
    return get_redis_connection().set(name=key, value=value, ex=ex, px=px, nx=nx, xx=xx)

'''
获取单个值
'''
def read_from_redis(key):
    value = get_redis_connection().get(key)
    return value

'''
key对应的value自增1
'''
def incrby_to_redis(key):
    return get_redis_connection().incrby(name=key)

'''
所有的list操作都定死为 lpush, rpop
left push to list, 可以批量操作
return: len(list)
'''
def push_to_list(key, *values):
    return get_redis_connection().lpush(key, *values)

'''
所有的list操作都定死为 lpush, rpop
left push if exist, 只可以单个操作
return: len(list)
'''
def push_to_list_exist(key, value):
    return get_redis_connection().lpushx(key, value)

'''
所有的list操作都定死为 lpush, rpop
return None for nil list
'''
def pop_from_list(key):
    return get_redis_connection().rpop(name=key)


'''
读出一个map
doJsonLoad: 是否帮我做每个字段的json load反解
'''
def read_from_redis_hash(key, doJsonLoad=True):
    mapping = get_redis_connection().hgetall(key)
    if doJsonLoad == False:
        return mapping

    if mapping is None:
        return {}

    ret = {}
    for map_key in mapping:
        ret[map_key.decode('utf-8')] = json.loads(mapping[map_key])

    return ret


'''
写入一个map
'''
def write_to_redis_hash(key, map):
    mapping = {}
    for map_key in map:
        mapping[map_key] = json.dumps(map[map_key])

    return get_redis_connection().hmset(key, mapping=mapping)
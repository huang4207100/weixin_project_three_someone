# -*- coding: utf-8 -*-

'''
这对一些时间的转换
'''

import time
from datetime import datetime, timedelta


#datetime对象 得到time string
def datetime_to_str(dt, format='%Y-%m-%d %H:%M:%S'):
    return dt.strftime(format)


#datetime对象 得到unix时间
def datetime_to_unix(dt):
    return int(time.mktime(dt.timetuple()))


#string      得到datetime对象
def str_to_datetime(t_string, format='%Y-%m-%d %H:%M:%S'):
    return datetime.strptime(t_string, format)

#string      得到unix时间
def str_to_unix(t_string, format='%Y-%m-%d %H:%M:%S'):
    dt = str_to_datetime(t_string=t_string, format=format)
    return datetime_to_unix(dt=dt)


#unix time   得到datetime对象
def unix_to_datetime(t):
    t = int(t)
    return str_to_datetime(t_string=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(t)) )

#unix_time   得到time string
def unix_to_str(t):
    dt = unix_to_datetime(t)
    return datetime_to_str(dt=dt)

#定义一个永不到期的截止时间
def forever_datetime():
    return datetime.now() + timedelta(days=365 * 1000)


#得到当天0点时间
def getOClockOfToday():
    t = time.localtime(time.time())
    time1 = time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', t), '%Y-%m-%d %H:%M:%S'))
    return int(time1)


#得到某天的0点时间
def getOClockOfSomeday(unix_t):
    '''
    得到某天的 0点时刻
    :param t: 属于某天的任意一个unix时间(int)
    :return: 得到那天的0点unix时间
    '''
    t = time.localtime(unix_t)
    time1 = time.mktime(time.strptime(time.strftime('%Y-%m-%d 00:00:00', t), '%Y-%m-%d %H:%M:%S'))
    return int(time1)

# 打印当前时间
def printConcurrentTime(prefix):
    print("%s -> %s" % (prefix, datetime.now()))





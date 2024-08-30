# -*- coding: utf-8 -*-

import sys
from urllib.request import quote
from urllib.request import pathname2url
from urllib.request import url2pathname
import datetime
import time
import SpiderTaskMysql


def OneceUrl(result):
    q1 = pathname2url(result[7]).replace("%2B", "+")
    q2 = pathname2url(result[9]).replace("%2B", "+")
    q3 = pathname2url(result[8]).replace("%2B", "+")
    q4 = pathname2url(result[10]).replace("%2B", "+")
    start_time = result[4]
    end_time = result[5]
    if end_time is None:
        end_time = int(time.mktime(datetime.date.today().timetuple()))
    else:
        end_time = int(time.mktime(end_time.timetuple()))
    if start_time is None:
        start_time = end_time - 60 * 60 * 24 * 30
    else:
        start_time = int(time.mktime(start_time.timetuple()))
    if (end_time - start_time) > 60 * 60 * 24 * 365:
        start_time = end_time - 60 * 60 * 24 * 365
    ft = result[11]
    q5 = result[12]
    q6 = result[13]
    tn = "baiduadv"

    if q6 is "":
        time_step = 60 * 60
    else:
        time_step = 60 * 60 * 24
    url = []
    while start_time < end_time:
        stop_time = start_time + time_step
        if stop_time > end_time:
            stop_time = end_time
        gpc_time = 'stf={start_time},{end_time}|stftype=1'.format(start_time=str(start_time), end_time=str(stop_time))
        gpc = pathname2url(gpc_time)
        sub_url = 'https://www.baidu.com/s?q1={}&q2={}&q3={}&q4={}&gpc={}&ft={}&q5={}&q6={}&tn{}'.format(q1, q2, q3, q4,
                                                                                                         gpc, ft, q5,
                                                                                                         q6,
                                                                                                         tn)
        url.append((sub_url,start_time))
        start_time = stop_time
    return url


def LastingUrl(result):
    q1 = pathname2url(result[7]).replace("%2B", "+")
    q2 = pathname2url(result[9]).replace("%2B", "+")
    q3 = pathname2url(result[8]).replace("%2B", "+")
    q4 = pathname2url(result[10]).replace("%2B", "+")
    end_time = int(time.mktime(datetime.date.today().timetuple()))
    start_time = result[4]
    if start_time is None:
        start_time = end_time - 60 * 60 * 24 * 3
    else:
        start_time = int(time.mktime(start_time.timetuple()))

    ft = result[11]
    q5 = result[12]
    q6 = result[13]
    tn = "baiduadv"

    if q6 is "":
        time_step = 60 * 60
    else:
        time_step = 60 * 60 * 24
    url = []
    while start_time < end_time:
        stop_time = start_time + time_step
        if stop_time > end_time:
            stop_time = end_time
        gpc_time = 'stf={start_time},{end_time}|stftype=1'.format(start_time=str(start_time), end_time=str(stop_time))
        gpc = pathname2url(gpc_time)
        sub_url = 'https://www.baidu.com/s?q1={}&q2={}&q3={}&q4={}&gpc={}&ft={}&q5={}&q6={}&tn{}'.format(q1, q2, q3, q4,
                                                                                                         gpc, ft, q5,
                                                                                                         q6,
                                                                                                         tn)
        url.append((sub_url,start_time))
        start_time = stop_time
    return url


def MakeUrl(result):
    if result is None:
        return None

    if result[3] == 1:
        return LastingUrl(result)
    else:
        return OneceUrl(result)


def MakeSiteUrl(result):
    if result is None:
        return None
    url = result[1]
    root_url = url[(url.index('//') + 2):]
    root_url = root_url[root_url.index('.') + 1:]
    root_url = root_url[0:root_url.index('/')]
    root_url = root_url.replace('.', '\.')
    re_string = '.*' + root_url + '/.*'
    return re_string

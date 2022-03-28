

import sys
import random

#是否开启https服务器的证书校验
allow_ssl_verify = False

#__________________________
# requests 配置项
# —————————————————————————

#超时时间
timeout = 10

#是否允许url重定向
allow_redirects = True

#是否允许继承http Request类的Session支持，在发出的所有请求之间保持cookies，
allow_http_session = True

#是否允许随机User-Agent
allow_random_useragent = False

#是否允许随机x-Forwarded-For
allow_random_x_forward = False

#随机HTTP头

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
    "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
    "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
    "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
    "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
    "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
]
#随机生成User-Agent
def random_useragent(condition=False):
    if condition:
        return random.choice(USER_AGENTS)
    else:
        return USER_AGENTS[0]

#随机x-Forwarded-For，动态ip
def random_x_forwarded_for(condition=False):
    if condition:
        return '%d.%d.%d.%d' %(random.randint(1,254),random.randint(1,254),random.randint(1,254),random.randint(1,254))

    else:
        return '8.8.8.8'

#HTTP头设置
headers = {
    'User-Agent':random_useragent(allow_random_useragent),
    'X_FORWARDED-FOR':random_x_forwarded_for(allow_random_x_forward),
    'ReFerer':'http://www.baidu.com',
    'Cookie':"",
}
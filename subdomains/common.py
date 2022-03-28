

from config import *
import re
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import requests
import json
def http_requests_get(url,allow_redirects=allow_redirects):
    try:
        result = requests.get(
            url = url,
            headers = headers,
            timeout = timeout,
            allow_redirects = allow_redirects,
            verify = allow_ssl_verify
        )
        return result
    except Exception as e:
        return e

def http_requests_post(url,payload,allow_redirects=allow_redirects):
    try:
        result = requests.get(
            url=url,
            date = payload,
            headers=headers,
            timeout=timeout,
            allow_redirects=allow_redirects,
            verify=allow_ssl_verify,
        )
        return result
    except Exception as e:
        return e

def is_domain(domain):
    #判断是否是域名的正则
    domain_regex = re.compile(
    r'(?:[A-Z0-9_](?:[A-Z0-9-_]{0,247}[A-Z0-9])?\.)+(?:[A-Z]{2,6}|[A-Z0-9-]{2,}(?<!-))\z',
        re.IGNORECASE)
    return True if domain_regex.match(domain) else False


def save_result(filename,result):
    try:
        f=open(filename,'w',encoding='utf8')
        json.dump(result,f,indent=4)

    except Exception as e:
        print(e)

def read_json(filename):
    try:
        f= open(filename,'r',encoding='utf8')
        datas = json.load(f)
        return datas
    except Exception as e:
        print(e)
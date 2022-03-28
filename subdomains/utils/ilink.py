from common import http_requests_post, is_domain
import re


class Ilink(object):
    def __init__(self, domain):
        self.domain = domain
        self.site = 'http：//i.links.cn/subdomain/'
        self.result = []

    def run(self):
        payload = {
            'domain':self.domain,
            'b2':1,
            'b3':1,
            'b4':1,
        }
        try:
            r = http_requests_post(self.site,payload)
            #查看返回内容
            return r.text
            results = re.findall('</TD>\n<TD>(.*?)</TD>\n <TD><A', r.text, re.S)

            for result in results:
                if is_domain(result):
                    self.result.append(result)
                return list(set(self.result))
            return self.result
# ------------------------------------------------------------
            # 先查看有哪些数据
            # self.result.append(r.text)
            # 然后过滤掉不必须的数据
            # results = re.findall('</TD>\n<TD>(.*?)</TD>\n <TD><A', r.text, re.S)
            #
            # for result in results:
            #     if is_domain(result):
            #         self.result.append(result)
            #     return list(set(self.result))
            # return self.result
# ------------------------------------------------------------
        except Exception as e:
            return self.result
#程序功能：C段web服务扫描；
#意义：
#1，信息搜集，找到目标系统所在c段的其他服务
#2，寻找短板 有可能找到目标系统其他存在的弱点
#3.资产识别 对于网络运维管理人员，可以发现c段内的资产信息

#程序设计
#requests+多线程，对目标段内的每一台主机，可能有web服务的端口发起请求。
#有服务就返回内容，无服务就报错

#设计点：
#1，指定端口或将扫描端口写死在程序中；
#线程数可控
#输出报表方便查看结果

# tips:
#1.该程序会对所有C段地址进行扫描；
   # a.引入nmap模块；
   # b.在外部，使用哪个nmap，zmap进行快速的扫描，将结果保存，再放入程序，进行扫描识别。
   # nmap -sn -PE --min-hostgroup 1024 --min-parallelism 1024 -oX nmap.xml $1
   # -sn 不进行端口扫描，只进行ping检测
   # -PE 通过ICMP echo来判定主机是否存活
    # --min-hostgroup 1024 最小分组设置1024个Ip地址
    # --min-parallelism 1024 将探针的数量设置最小为1024


import requests
from queue import Queue
import threading
import time
import sys
from IPy import IP
import re

HEADERS={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36 Edg/89.0.774.77"}

class DirScan(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self._queue = queue

    def run(self):
        while not self._queue.empty():
            url = self._queue.get()
            # try:
            #     print(url)
            # except:
            #     pass
            try:
                r = requests.get(url=url,timeout=6,headers = HEADERS)
                if r.status_code ==200:
                    print('[*]web service Found!%s'%url)
                    try:
                        title = re.findall('<title>(.*?)</title>',r.text)[0]
                    except:
                        title='None'

                    print(url+':'+title)
                    f= open('result.html','a+')
                    f.write('<a href="'+url+'" target="_blank">'+url+'</a>'+'\t\t'+title+'\n')
                    f.write('<br>')
                    f.close()
            except Exception as e:
                print(e)
                pass

def create(ips):
    queue = Queue()
    # ip = IP(ips,make_net=True)
    req_m = ['http://',]
    #指定端口
    ports = ['80','8080','3443',]
    #追加web目录
    dirs = ['','/phpmyadmin','/admin','/temp']

    for h in req_m:
        for i in ips:
            for j in ports:
                for k in dirs:
                    queue.put(str(h)+str(i)+':'+str(j)+str(k))
    return queue

def main(ips):
    f=open('result.html','w')
    f.close()
    queue = create(ips)
    threads = []

    thread_count = 10
    for i in range(thread_count):
        threads.append(DirScan(queue))

    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    with open('nmap.xml') as f:
        ips = re.findall('<addres addr="(.*?)" addrtype=>',f.read())
        main(ips)
    # if len(sys.argv) ==2:
    #     start = time.time()
    #     main(sys.argv[1])
    #     print(time.time()-start)
    #     sys.exit(0)
    # else:
    #     print('usage:%s 192.168.1.1/24'%(sys.argv[0]))
    #     sys.exit(-1)

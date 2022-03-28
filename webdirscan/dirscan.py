#程序功能解读
#1.基本功能：目录扫描，敏感文件扫描
#目录和文件字典
#程序取出字典内容，和目标网站拼接，进行请求识别
#设计思路：1，目录字典文件能否指定；2.线程数可控；3，扩展至BurpSuite。


import requests
from queue import Queue
import sys
import threading
from agent_proxy import user_agent_list
from optparse import OptionParser

class DirScanMain:
    def __init__(self,options):
        self.url =options.url
        self.ext = options.ext
        self.count = options.count

    class DirScan(threading.Thread):
        def __init__(self,queue,total):
            threading.Thread.__init__(self)
            self._queue = queue
            self._total = total

        def run(self):
            while not self._queue.empty():
                url = self._queue.get()
                #print url
                threading.Thread(target=self.msg).start()

                try:
                    r = requests.get(url=url,headers = user_agent_list.get_user_agent(),timeout=8,)
                    if r.status_code == 200:
                        # print('[*]'+url)
                        sys.stdout.write('\r'+'[*]%s\t\t\n'%(url))
                        f = open('result.html','a+')
                        f.write('<a href="'+url+'" target="_blank">'+url+'</a>')
                        f.write('\r\n</br>')
                        f.close()
                except Exception as e:
                    pass
        def msg(self):
            # print(self._total,self._queue.qsize())
            per =100-float(self._queue.qsize())/float(self._total)*100
            # print('%1.f'%per)
            msg='%s Left| %s All| Scan in %1.f %s'%(self._queue.qsize(),self._total,per,'%')
            sys.stdout.write('\r'+'[*]'+msg)
    def start(self):
        f = open('result.html','w')
        f.close()
        queue = Queue()

        f=open('./dics/%s.txt'%self.ext,'r')
        for i in f:
            queue.put(self.url+i.rsplit('\n'))
        total = queue.qsize()

        threads = []
        thread_count = self.count

        for i in range(thread_count):
            threads.append(self.DirScan(queue))
        for t in threads:
            t.start()
        for t in threads:
            t.join()
if __name__ == '__main__':
    # if len(sys.argv) !=4:
    #     sys.exit(-1)
    # else:
    #     start(sys.argv[1],sys.argv[2],sys.argv[3])
    print('''
  _____  _      _____                 
 |  __ \(_)    / ____|                
 | |  | |_ _ _| (___   ___ __ _ _ __  
 | |  | | | '__\___ \ / __/ _` | '_ \ 
 | |__| | | |  ____) | (_| (_| | | | |
 |_____/|_|_| |_____/ \___\__,_|_| |_|
                                      ''')

    parser = OptionParser()
    parser.add_option('-u','--url',dest='url',help='target url for scan')
    parser.add_option('-f','--file',dest = 'target url ext')
    parser.add_option('-t','--thread',dest='count',default=10,help='scan thread_count')

    (options,args) = parser.parse_args()

    if options.url and options.ext:
        d=DirScanMain(options)
        d.start()
        sys.exit()
    else:
        parser.print_help()
        sys.exit(1)
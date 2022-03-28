
import dns.resolver
import threading
from queue import Queue
from config import *
import sys

class BruteDns(object):
    def __init__(self,domain):
        self.domain = domain
        self.thread_count = thread_count
        self.queue = Queue()
        self.result = []

    def run(self):
        #字典文档
        with open('dicts/subnames.txt') as f:
            for i in f:
                self.queue.put(i.rstrip()+'.'+self.domain)
        total = self.queue.qsize()
        threads =[]
        for i in range(self.thread_count):
            threads.append(self.BruteRun(self.queue,self.result))
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        return list(set(self.result))

    class BruteRun(threading.Thread):
        def __init__(self,queue,result):
            threading.Thread.__init__(self)
            self._queue = queue
            self.result =result
            self.total = total

        def run(self):
            while not self._queue.empty():
                sub = self._queue.get_nowait()
                try:
                    results = dns.resolver.query(sub,'A')
                    if results.response.answer:
                        self.result.append(sub)

                except Exception as e:
                    pass

        def msg(self):
            done_count = self.total - self._queue.qsize()
            all_count = self.total
            found_count = len(self.result)
            msg = '\t[-]Last{} | Complete{:.2f}% | Found {}'.format(self._queue.qsize(),(done_count/all_count)*100,found_count)
            sys.stdout.write('\r'+msg)
            sys.stdout.flush()
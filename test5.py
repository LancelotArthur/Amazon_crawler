from urllib.request import *
import socket
import time
from header import *
from test4 import *
import random
import threading
import queue

socket.setdefaulttimeout(60)

class thread_crawler(threading.Thread):
    def __init__(self, q, tc_id):
        threading.Thread.__init__(self)
        self.q = q
        self.id = tc_id
        self.count = 0

    def run(self):
        while not self.q.empty():
            ASIN = self.q.get()
            url = 'https://www.amazon.com/dp/' + ASIN
            #print(url)
            headers = randHeader()
            req = Request(url=url, headers=headers)
            try:
                urlopen(req, timeout = 60000)
                page = urlopen(req).read().decode()
                f3 = open('xxx' + str(self.id) + '.txt', 'w', errors='ignore')
                f3.write(page)
            except Exception as e:
                print('404')
                continue
            parse(self.id, ASIN)
            self.count = self.count + 1
            print(str(self.id) + ':' + str(self.count))

    def get_count(self):
        return self.count

q = queue.Queue(maxsize=503)
threads = []
count = 0


def queue_fill(f):
    i = 0
    for line in f:
        if line:
            q.put(str(line))
            i = i + 1
            if i > 40:
                i = 0
                yield
        else:
            return


def threads_init():
    for i in range(5):
        thread = thread_crawler(q, i)
        thread.start()
        threads.append(thread)
        time.sleep(3)


def threads_kill():
    global count
    global threads
    for t in threads:
        t.join()
        count = count + t.get_count()
    threads = []


def make_5_to_1():
    fzyj = open('resource.txt', 'w', errors='ignore')
    for i in range(5):
        frr = open('zyj' + str(i) + '.txt', 'r')
        for line in frr:
            fzyj.write(line)
        frr.close()
    fzyj.close()
    #clear
    for i in range(5):
        frr = open('zyj' + str(i) + '.txt', 'w')
        frr.close()


def main():
    #global q
    print('start...\n')
    flag = 0
    while True:
        '''
        fill queue and crawl.
        '''
        f_resource = open('resource.txt', 'r', errors='ignore')
        qf = queue_fill(f_resource)
        while True:
            try:
                qf.send(None)
            except Exception as e:
                break
            if q.empty():
                break
            threads_init()
            threads_kill()
        f_resource.close()
        make_5_to_1()#fresh resource.txt
        import os
        if os.path.getsize('resource.txt') < 5:
            break
    print(count)
    print('finish...')

if __name__ == '__main__':
    main()
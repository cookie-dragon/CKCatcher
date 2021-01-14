#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project_ = 'CKCatcher'
__file_name__ = 'test2'
__author__ = Cooky Long
__time__ = '20210114T1945'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃        ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import threading
import time

from crawler.pandc.consumers import Consumers
from crawler.pandc.queues import Queues


class Producer(threading.Thread):
    def run(self):
        global queues

        for i in range(100):
            queues.put('OBJ' + str(i))
            time.sleep(0.1)


class Consumer(threading.Thread):
    def run(self):
        global queues
        while True:
            obj = queues.get()
            if obj is None:
                time.sleep(0.2)


if __name__ == '__main__':
    queues = Queues()
    # p = Producer()
    # p.start()

    for i in range(30):
        queues.put('OBJ' + str(i))
        time.sleep(0.1)

    time.sleep(1)

    c = Consumers(queues=queues)
    c.start()

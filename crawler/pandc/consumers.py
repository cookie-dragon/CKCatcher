#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project_ = 'CKCatcher'
__file_name__ = 'consumers'
__author__ = Cooky Long
__time__ = '20210114T2030'
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


class Consumers(object):
    class Consumer(threading.Thread):
        def __init__(self, queues, consumer_list):
            super().__init__()
            self.queues = queues
            self.consumer_list = consumer_list

        def run(self):
            cnt_none = 0
            cnt_empty = 0
            while cnt_none > 3 and cnt_empty > 3:
                obj = self.queues.get()
                if obj is None:
                    cnt_none += 1
                    if self.queues.size() == 0:
                        cnt_empty += 1
                    else:
                        cnt_none = 0
                        cnt_empty = 0

                    if self.consumer_list.index(self) != 0:
                        time.sleep(0.2)
                    else:
                        time.sleep(1)
                else:
                    cnt_none = 0
                    cnt_empty = 0
            if self.consumer_list.index(self) == 0:
                print('0号消费者退出')

    def __init__(self, queues, cnt=3):
        self.consumer_list = []
        for i in range(cnt):
            self.consumer_list.append(Consumers.Consumer(queues=queues, consumer_list=self.consumer_list))

    def start(self):
        for consumer in self.consumer_list:
            consumer.start()

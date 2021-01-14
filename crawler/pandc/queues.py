#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project_ = 'CKCatcher'
__file_name__ = 'queues'
__author__ = Cooky Long
__time__ = '20210114T1955'
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
from queue import Queue


class Queues(object):
    def __init__(self, cnt=3, maxsize=16):
        self.queue_list = []
        for i in range(cnt):
            self.queue_list.append(Queue(maxsize=maxsize))

    def size(self):
        return len(self.queue_list)

    def sum(self):
        sum = 0
        for queue in self.queue_list:
            sum += queue.qsize()
        return sum

    def ave(self):
        return self.sum() / self.size()

    def put(self, object):
        put_success = False
        for queue in self.queue_list:
            if queue.qsize() <= self.ave():
                queue.put(object)
                print('将[' + str(object) + ']放入队列' + str(self.queue_list.index(queue)))
                put_success = True
                break
        if not put_success:
            self.queue_list[0].put(object)
            print('WARNING放置错误 - 强制将[' + str(object) + ']放入队列0')

    def get(self):
        object = None
        if self.sum() > 0:
            get_success = False
            for queue in self.queue_list:
                if queue.qsize() >= self.ave():
                    object = queue.get()
                    print('将[' + str(object) + ']从队列' + str(self.queue_list.index(queue)) + '中取出')
                    get_success = True
                    break
            if not get_success:
                print('ERROR取出失败！！！')
        else:
            print('队列空了，没东西拿')
        return object

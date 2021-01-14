#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 10:41 上午
# @Author  : Cooky Long
# @File    : novel
import requests
from bs4 import BeautifulSoup


class Novel(object):

    def __init__(self, bookurl):

        self.url_book = bookurl

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 12:37 下午
# @Author  : Cooky Long
# @File    : catcher
import requests
from bs4 import BeautifulSoup


class Catcher(object):

    def __init__(self, url, session=None):
        requests.packages.urllib3.disable_warnings()

        self.url = url
        if session is None:
            self.session = requests.Session()
        else:
            self.session = session

    def _getsoup(self, url, encoding='utf-8', features='html.parser'):
        response = self.session.get(url, verify=False)
        response.encoding = encoding
        page = response.text
        soup = BeautifulSoup(markup=page, features=features)
        return soup

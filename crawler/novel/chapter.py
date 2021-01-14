#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 12:36 下午
# @Author  : Cooky Long
# @File    : chapter
from crawler.novel.catcher import Catcher


class Chapter(Catcher):
    def __init__(self, url, session=None):
        super().__init__(url, session)

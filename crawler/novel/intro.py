#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 12:49 下午
# @Author  : Cooky Long
# @File    : intro
from crawler.novel.catcher import Catcher


class Intro(Catcher):
    def __init__(self, url, session=None):
        super().__init__(url, session)

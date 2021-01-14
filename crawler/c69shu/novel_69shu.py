#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 10:47 上午
# @Author  : Cooky Long
# @File    : c69shu
from crawler.c69shu import url_index
from crawler.novel.novel import Novel


class Novel69shu(Novel):

    def __init__(self, bookid, is_url=False):
        if is_url:
            bookurl = bookid
            self.id_book = -1
        else:
            self.id_book = bookid
            bookurl = self.__get_bookurl()
        super().__init__(bookurl)

    def __get_bookurl(self):
        return url_index + '/book/' + self.id_book + '/'

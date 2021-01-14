#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 10:56 上午
# @Author  : Cooky Long
# @File    : intro
from crawler.novel import intro


class Intro(intro.Intro):
    def __init__(self, url, session=None):
        super().__init__(url, session)

    def get(self):
        intro = {}
        soup = self._getsoup(self.url, encoding='gbk')
        book_info = soup.html.body(
            'div', {'class': 'box nopad border', 'id': 'box-info'})[0](
            'div', {'class': 'book_info'})[0]
        intro['coverurl'] = book_info(
            'div', {'class': 'pic'})[0].img['src'].strip()
        info = book_info(
            'div', {'id': 'info'})[0]
        intro['title'] = info.h1.text.strip()
        intro['author'] = info.h1.small.a.text.strip()
        intro['desc'] = info(
            'div', {'class': 'bookinfo_intro'})[0].text.strip()
        return intro
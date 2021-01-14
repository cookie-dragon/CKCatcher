#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project_ = 'CKCatcher'
__file_name__ = 'chaptes'
__author__ = Cooky Long
__time__ = '20210114T1730'
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
from crawler.novel import chapters


class Chapters(chapters.Chapters):
    def __init__(self, url, url_prefix, session=None):
        super().__init__(url, session)
        self.url_prefix4chapter = url_prefix

    def get(self):
        chapterlist = []

        soup = self._getsoup(self.url, encoding='gbk')
        lis = soup.html.body(
            'div', {'class': 'box nopad border'})[1](
            'div', {'class': 'book_list'})[0](
            'ul', {'class': 'chapterlist'})[1]('li', {'class': False})
        for li in lis:
            if li.a:
                chapterurl = self.url_prefix4chapter + li.a['href']
                chaptertitle = li.a.text.strip()
                chapterlist.append((chapterurl, chaptertitle))

        return self.url, chapterlist

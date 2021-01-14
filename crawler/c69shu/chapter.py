#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 12:36 下午
# @Author  : Cooky Long
# @File    : chapter
from crawler.novel import chapter


class Chapter(chapter.Catcher):
    def __init__(self, url, session=None):
        super().__init__(url, session)
        self.blackliststrline = ['一秒记住【69书吧www.69shu.io】，更新快，无弹窗，免费读！', ' 69书吧 www.69shu.io，最快更新']
        self.blackliststr = []

    def get_lines(self):
        lines = []

        soup = self._getsoup(self.url, encoding='gbk')
        contentbox = soup.html.body(
            'div', {'class': 'box nopad border'})[0](
            'div', {'class': 'ncon', 'id': 'content'})[0](
            'div', {'class': 'nc_l', 'id': 'jsnc_l'})[0](
            'div', {'class': 'wrapper_main'})[0](
            'div', {'class': 'contentbox clear', 'id': 'htmlContent'})[0]
        textlines = contentbox(text=True)
        for line in textlines:
            if line not in self.blackliststrline:
                line = line.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '').strip()
                if line not in self.blackliststrline:
                    if line != '':
                        for blackstr in self.blackliststr:
                            if blackstr in line:
                                line.replace(blackstr, '')
                        lines.append(line)

        return lines

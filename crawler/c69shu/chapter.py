#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 12:36 下午
# @Author  : Cooky Long
# @File    : chapter
from crawler.novel import chapter


class Chapter(chapter.Catcher):
    def __init__(self, url, session=None):
        super().__init__(url, session)
        # 整行匹配（replace前后都要判断）并整行删除
        self.blackliststrline = ['一秒记住【69书吧www.69shu.io】，更新快，无弹窗，免费读！', ' 69书吧 www.69shu.io，最快更新', '最新章节！']
        # 部分匹配（replace后[部分匹配并部分删除]前判断）并整行删除
        self.blackliststr2delall = []
        # 部分匹配（replace后判断）并部分删除
        self.blackliststr = []

    def get(self):
        lines = []

        soup = self._getsoup(self.url, encoding='gbk')
        wrapper_main = soup.html.body(
            'div', {'class': 'box nopad border'})[0](
            'div', {'class': 'ncon', 'id': 'content'})[0](
            'div', {'class': 'nc_l', 'id': 'jsnc_l'})[0](
            'div', {'class': 'wrapper_main'})[0]
        title = wrapper_main(
            'h1', {'class': 'h1title'})[0].text.strip()
        contentbox = wrapper_main(
            'div', {'class': 'contentbox clear', 'id': 'htmlContent'})[0]
        textlines = contentbox(text=True)
        for line in textlines:
            if line not in self.blackliststrline:
                line = line.replace('\r', '').replace('\n', '').replace('\t', '').replace(' ', '').strip()
                if line not in self.blackliststrline:
                    if line != '':
                        noline2del = True
                        for blackstr2delall in self.blackliststr2delall:
                            if blackstr2delall in line:
                                noline2del = False
                                break
                        if noline2del:
                            for blackstr in self.blackliststr:
                                if blackstr in line:
                                    line.replace(blackstr, '')
                            lines.append(line)

        return self.url, title, lines

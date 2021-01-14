#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 10:31 上午
# @Author  : Cooky Long
# @File    : test
from crawler.c69shu.chapter import Chapter
from crawler.c69shu.intro import Intro

if __name__ == '__main__':
    intro = Intro(url='https://www.69shu.io/book/115541/')
    dict_intro = intro.get()
    print('')

    chapter = Chapter(url='https://www.69shu.io/book/115541/47641563.html')
    lines = chapter.get_lines()
    print('')

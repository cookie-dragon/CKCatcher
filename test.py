#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/14 10:31 上午
# @Author  : Cooky Long
# @File    : test
import requests

from crawler.c69shu.chapter import Chapter
from crawler.c69shu.chapters import Chapters
from crawler.c69shu.intro import Intro
from crawler.c69shu.novel_69shu import Novel69shu

if __name__ == '__main__':
    session = requests.Session()

    novel = Novel69shu(bookid='115541')
    print('初始化：' + novel.url_book)

    intro = Intro(url=novel.url_book, session=session)
    rtn_intro = intro.get()
    print('获取简介：' + rtn_intro[1]['title'] + '-' + rtn_intro[1]['author'])

    chapters = Chapters(url=novel.url_book, url_prefix=novel.url_book, session=session)
    rtn_chapters = chapters.get()
    print('获取所有章节地址：一共' + str(len(rtn_chapters[1])) + '章')

    for chapterurl, chaptertitle in rtn_chapters[1]:
        chapter = Chapter(url=chapterurl, session=session)
        chapter.blackliststrline.append(rtn_intro[1]['title'])
        rtn_chapter = chapter.get()
        print('外置标题：' + chaptertitle + ' \t 获取章节内容：' + rtn_chapter[0] + ' \t ' + rtn_chapter[1] + ' \t 一共' + str(
            len(rtn_chapter[2])) + '行')

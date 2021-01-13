#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
__project_ = 'CKCatcher'
__file_name__ = 'app'
__author__ = Cooky Long
__time__ = '20210113T2124'
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
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from ui import QTMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 初始化app
    main_window = QMainWindow()  # 创建主窗口
    main_ui = QTMainWindow.Ui_MainWindow()  # 创建UI界面
    main_ui.setupUi(main_window)  # 初始化UI到主窗口，主要是建立代码与ui之间的signal与slot
    main_window.show()  # 显示窗口
    sys.exit(app.exec_())  # 消息循环结束之后返回0，接着调用sys.exit(0)退出程序

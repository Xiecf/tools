#!/usr/bin/python
# -*- coding: utf-8 -*-

"""循环打印字符串,每次都把最后一个字符砍掉"""


# 无法打印完整字符串
def section_1(s):
    s = str(s)
    i = -1
    for i in range(-1, -len(s), -1):
        print(s[:i])


# 语法有误,待修正
def section_2(s):
    s = str(s)
    i = -1
    for i in [None] + range(-1, -len(s), -1):
        print(s[:i])



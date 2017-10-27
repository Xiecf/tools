#!/usr/bin/python
# -*- coding: utf-8 -*-

"""循环打印字符串,每次都把最后一个字符砍掉"""


# 无法打印完整字符串
def section_1(s):
    s = str(s)
    i = -1
    for i in range(-1, -len(s), -1):
        print(s[:i])


def section_2(s):
    s = str(s)
    i = -1
    list_1 = [None] + list(range(-1, -len(s), -1))
    for i in list_1:
        print(s[:i])


section_2('abcde')


def section_3(s):
    s = str(s)
    i = 1
    for i in range(len(s) + 1):
        print(s[:i])


section_3('abcde')
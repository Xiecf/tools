#!/usr/bin/python
# -*- coding: utf-8 -*-

import math


def quadratic(a, b, c):
    for i in [a, b, c]:
        if not isinstance(i, (int, float)):
            raise TypeError

    x3 = b ** 2 - 4 * a * c
    if a == 0:
        print('只有一个实数解')
        print(-c / b)
    else:
        if x3 < 0:
            print('此方程无实数解')
        elif x3 == 0:
            print('只有一个实数解')
            print(-b / (2 * a))
        else:
            print('有两个实数解')
            x1 = ((-b + math.sqrt(x3)) / (2 * a))
            x2 = ((-b - math.sqrt(x3)) / (2 * a))
            print(x1, x2)

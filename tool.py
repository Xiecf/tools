# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 18:22:18 2017

@author: xie
"""


def find(list, x):
    """枚举法进行线性搜索"""
    for i in range(len(list)):
        if list[i] == x:
            return i
    else:
        return -1


def find2D(matrix,row,column,x):
    """枚举法进行矩阵搜索"""
    for i in range(row):
        for j in range(column):
            if matrix[i][j] == x:
                return i + 1, j + 1
    return -1


# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:21:30 2018

@author: LZC
"""

def facto_L(num):
    F = 1
    if not num:
        # print(num, '阶乘为：', F)
        return F

    for i in range(num):
        F *= num - i
    return F
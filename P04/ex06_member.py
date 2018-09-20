# -*- coding:UTF-8 -*-
#! /usr/bin/python3
a = 1
b = 20

list_1 = [1,2,3,4,5]
if a in list_1: # 成员运算符
    print('a属于list_1')
else:
    print('a不在list_1')

if b not in list_1:
    print('b不属于list_1')
else:
    print('b属于list_1')

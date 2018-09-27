# -*- coding:UTF-8 -*-
#! /usr/bin/python3
# 伏波纳希数列
a,b = 0,1
while b<2000:
    print(b,end=' ')
    a,b = b,a+b # 右边的表达式会在赋值变动之前执行。右边表达式的执行顺序是从左往右的。

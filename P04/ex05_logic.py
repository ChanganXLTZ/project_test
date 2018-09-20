# -*- coding:UTF-8 -*-
#! /usr/bin/python
a = 10
b = 20
# 逻辑运算符
if a and b:
    print("a和b都为true")
else:
    print("a和b不都为true")

if a or b:
    print("a和b至少一个为true")
else:
    print("a和b都不为true")
a = 0
print()
if a and b: # 布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。
    print("a和b都为true")
else:
    print("a和b不都为true")

if a or b: # 布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。
    print("a和b至少一个为true")
else:
    print("a和b都不为true")

if a or not b: # 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
    print("a和b至少一个为true")
else:
    print("a和b都不为true")
print(not b)
print(not a)
print(b and not a)
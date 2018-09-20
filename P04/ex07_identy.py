# -*- coding:UTF-8 -*-
#! /usr/bin/python3
# 身份运算符：身份运算符用于比较两个对象的存储单元
# id() 函数用于获取对象内存地址。
a = 10
b = 10
if a is b :
    print('a 和 b 有相同的标识')# x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
else:
    print('a 和 b 没有相同的标识')

if id(a) == id(b):
    print('a 和 b 有相同的标识')
else:
    print('a 和 b 没有相同的标识')

a += 1
if a is not b :
    print('a 和 b 没有相同的标识')# x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
else:
    print('a 和 b 有相同的标识')

if id(a) != id(b):
    print('a 和 b 没有相同的标识')
else:
    print('a 和 b 有相同的标识')

a = b
if a is b :
    print('a 和 b 有相同的标识')
else:
    print('a 和 b 没有相同的标识')

if id(a) == id(b):
    print('a 和 b 有相同的标识')
else:
    print('a 和 b 没有相同的标识')
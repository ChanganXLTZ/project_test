# -*- coding:UTF-8 -*-
#! /usr/bin/python3
a = 10 # 1010
b = 15 # 1111
# 位运算符
print("按位与：",a&b) # 参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
print("按位或：",a|b) # 只要对应的二个二进位有一个为1时，结果位就为1。
print("按位异或：",a^b) # 当两对应的二进位相异时，结果为1
print("按位取反：",~a) # 对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1
print("按位左移：",b<<2) # 运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
print("按位右移：",b>>2) # 把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数。

#!/usr/bin/env python
# -*- coding:UTF-8 -*-
a = 2
b = 10
print('a+b:',a+b)
print('a*b:',a*b)
print('a/b:',a/b)
print('a//b:',a//b)
print('a%b:',a%b)
print('a**b:',a**b)

print('正常除法结果的数据类型：',type(10/2)) # 正常除法，能整除开也返回浮点型
print('整除运算结果的数据类型：',type(a//b)) # 整除，返回整型
print('浮点数整除结果的数据类型：',type(12.2//3.4))#混合计算默认转换成float型

i_a = a+2j
i_b = complex(a,b)
print('实部类型：',type(i_a),'虚部类型：',type(i_b)) # 复数的实部a和虚部b都是浮点型
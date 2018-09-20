#!/usr/bin/env python
# -*- coding:UTF-8 -*-
a = 2
b = 10
print(a+b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

print(type(a/b)) # 正常除法
print(type(a//b)) # 整除，混合计算默认转换成float型

i_a = a+2j
i_b = complex(a,b)
print(type(i_a),"\n" , type(i_b)) # 复数的实部a和虚部b都是浮点型
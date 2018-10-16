# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:27:07 2018

@author: LZC
"""

import Factorial as Fa
# import Fun_0.Fibonacci as Fi
from Fun_0 import Fibonacci as Fi
a= 0
F1 = Fa.facto_L(a)
print(a,'的阶乘为：',F1)
a= 5
F2 = Fa.facto_L(a)
print(a,'的阶乘为：',F2)

c = 60
F3 = Fi.Fibo(c)
print(c,'以内的费波纳希数列：',F3)
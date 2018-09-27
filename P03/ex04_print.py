#!/usr/bin/env python3
from __future__ import print_function
import sys; # 不同语句用分号隔开可以同行
x = 'first run';sys.stdout.write(x+'\n'+x)

print("a")
print("b") #默认换行输出
print("a",end="") #不换行输出
print("b",end="->")
print("c",end=" ")
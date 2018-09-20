# -*- coding:UTF-8 -*-
#! /usr/bin/python3
list_a = list(range(5,10))
it = iter(list_a)
print(next(it))
print(next(it))

for a in it:
    print(a,end=' ')

del it
import sys
list_b = range(4)
it = iter(list_b)

while 1:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

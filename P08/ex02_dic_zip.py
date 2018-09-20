# -*- coding:UTF-8 -*-
#! /usr/bin/python3

lista = [1,2,3,4]
listb = ['A','B','C','D']

for a,b in zip(lista,listb):
    print('Number:{0}.W:{1}.'.format(a,b))
# zip 使用方法
import sys
print(sys.path)

if __name__ == '__main__':
    print(dir())
str_a = repr('Rick\n')
print(str_a)
set_1 = set(str_a)
print(set_1)

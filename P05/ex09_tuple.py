# -*- coding:UTF-8 -*-
#! /usr/bin/python3
print('\n\b=====元组=====\n元组的两种定义方式：')
tup2 = (1,2,3,'1','2','3','a','s','d')
print(tup2)
tup1 =  1,2,3,4 # 不适用括号也可
print(tup1)

tup3 = () # 空元组
list1 = ["234","as","af",1]
print('数据类型转换：')
print(list1,'->',end = '')
tup3 = tuple(list1) # 数据类型转换

print(tup3)
print(type(tup3))
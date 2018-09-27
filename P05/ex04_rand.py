# -*- coding:UTF-8 -*-
#! /usr/bin/python3
import random

list_a = [1,2,3,4,1,2,3,4,5,1,4,3,4,1,10]
print(range(10))
print('将range(10)转化成数组：',list(range(10)))
print(random.choice(list_a))
print(random.choice(range(10)))
# print(random.randrange(-10,10,1.5)) # randrange ([start,] stop [,step])
print(random.random()) # 随机生成下一个实数，它在[0,1)范围内。
print(random.shuffle(list_a)) # 将序列的所有元素随机排序。
print(random.uniform(-10,10)) # 随机生成实数，它在[x,y]范围内。
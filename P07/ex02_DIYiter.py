# -*- coding:UTF-8 -*-
#! /usr/bin/python3
class myNumber:
    def __iter__(self):
        self.a = 2
        return self

    def __next__(self):
        x = self.a
        self.a += 2
        return x

Number_1 = myNumber()
N_iter = iter(Number_1)
# 仅输出偶数的迭代器
print('自定义迭代器')
print(next(N_iter))
print(next(N_iter))
# -*- coding:UTF-8 -*-
#! /usr/bin/python3

sub_opsitive = lambda a,b: abs(a-b)
print(sub_opsitive(123,1345))

a = 1
def local_var(x):
    global a # 需要使用 global 关键字声明
    print(a+x)

local_var(10)

def out():
    num = 10
    print('第一次输出：',num)
    def iner():
        nonlocal num ## nonlocal关键字声明
        num = 12
        print('调用iner时输出：',num)
    iner()
    print('调用out时输出：',num)

out()
# -*- coding:UTF-8 -*-
#! /usr/bin/python3
def dprint(str):
    print(str)
#    return

def fun_1(x):
    x += 1
    return x

def fun_2(x):
    x = [x,[123,12,1]]
    print('函数内a:', x)
    return x

def fun_3(x):
    x.append([1,2,3,4])
    print('函数内a:',x)
    return b
dprint("1") # return 存在与否尚无影响

a = 10
b = fun_1(a)
print('由于a属于不可变型，函数不会改变a的值',b,' ',a)

a = [10,11]
b = fun_2(a) # 输入变量未改变
print(b);print(a)

a = [10,11]
b = fun_3(a) # 输入变量已改变
print('函数外a:',a,'函数外b:',b)
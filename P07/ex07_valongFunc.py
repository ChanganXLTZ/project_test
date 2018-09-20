# -*- coding:UTF-8 -*-
#! /usr/bin/python3
def print_vary(var1,var2,*var3):# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
    var4 = var1+var3[0]
    var5 = var2+var3[-1]
    return var4,var5
[get1,get2] = print_vary(23,134,39,14,1515,16)
print(get1)
print(get2)
get3 = print_vary(12,3,214,14,15,125,5)
print(get3)
def print_vary_b(var1,var2,**var3):#加了两个星号 ** 的参数会以字典的形式导入。
    temp = list(var3.keys()) # 注意此处进行了类型转换
    var4 = var1+var3[temp[0]]
    var5 = var2+var3[temp[-1]]
    return var4,var5
get4 = print_vary_b(23,134,a = 14,b = 1515,c = 16)
print(get4)
def about_star(a,*,c,cc):# 声明函数时，参数中星号 * 可以单独出现，如果单独出现星号 * 后的参数必须用关键字传入。
    return  a + c + cc**2
# print(about_star(1,2,3)) # 直接调用会报错
print(about_star(1,cc = 20,c = 10)) # 关键字
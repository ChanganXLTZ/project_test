#!/usr/bin/env python3
tuple_a = ("asd",1,1.2,"qwe")
tuple_b = ("12as",2)
print(tuple_a)
print(tuple_a[:1]) # 显示有个逗号
print(tuple_b[0])
print(tuple_a[2:4])
print(tuple_b *4)
print(tuple_a + tuple_b) # 元组元素无法修改
tuple_e = () # 空元组

tuple_sigle = (1,) # 单元素元组创建需要有逗号
print(type(tuple_sigle))
tuple_sigle2 = (1) # 此种定义方式将定义成 int 型
print(type(tuple_sigle2))
# 当元组包含可变型变量
tuple_l = ([1.1],123)
# print(type(tuple_l(0)))

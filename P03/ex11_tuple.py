#!/usr/bin/env python3
print('Python元组')
tuple_a = ("asd",1,1.2,"qwe")
tuple_b = ("12as",2)
print('定义元组1：',tuple_a)
print('元组可以切割：',tuple_a[:1]) # 显示有个逗号
print('元组2的第一个元素：',tuple_b[0])
print('元组1切割：',tuple_a[2:4])
print('元组重复显示：',tuple_b *4)
print('元组可以连接:',tuple_a + tuple_b) # 元组元素无法修改
tuple_e = () # 空元组

print('\n\b单元素元组创建需要有逗号，定义语法为：(1,) ')
tuple_sigle1 = (1,) # 
print('变量的值：',tuple_sigle1)
print('变量的类型：',type(tuple_sigle1))
print('此种定义方式将定义成 int 型，定义语法为：(1) ')
tuple_sigle2 = (1) # 
print('变量的值：',tuple_sigle2)
print('变量的类型：',type(tuple_sigle2))

# 当元组包含可变型变量
print('\n\b当元组包含可变型变量')
tuple_l = ([1.1,1],123)
print(type(tuple_l))

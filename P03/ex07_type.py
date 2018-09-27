#!/usr/bin/env python3
a = b = c = 1 # 该语句表示创建一个整型对象，值为 1，从后向前赋值，三个变量都指向同一个内存地址。
d,e,f = 2, 3,"F" # 两个整型对象 1 和 2 的分配给变量 d 和 e，字符串对象 "F" 分配给变量 f。
print('目前变量的值：',a,b,c,d,e,f)
print('变量a的数据类型：',type(a)) # 查看变量类型
if_b_bool = isinstance(b,bool) # 判断变量类型
if if_b_bool:
    print('b是布尔型变量')
else:
    print('b不是布尔型变量')


class A: pass 
class B(A):pass # A为父类
print('\n\bisinstance函数也可用于比较变量类型是否相同')
print(type(B)) 
print(type(B())) 
print(isinstance(A(),A))
print(type(A()) == A)
print(isinstance(A(),B))
print(type(A()) == B)
print(isinstance(B(),B))
print(type(B()) == B)
# print(type(B()) == type(B)) # ???
print(isinstance(B(),A))
print(type(B()) == A)

print('注：isinstance() 会认为子类是一种父类类型。\n    type() 不会认为子类是一种父类类型。')
'''
del A,B
print(isinstance(A(),A)) # 报错：未定义
'''
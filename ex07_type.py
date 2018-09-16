#!/usr/bin/env python3
a = b = c = 1 # 该语句表示创建一个整型对象，值为 1，从后向前赋值，三个变量都指向同一个内存地址。
d,e,f = 2, 3,"F" # 两个整型对象 1 和 2 的分配给变量 d 和 e，字符串对象 "F" 分配给变量 f。
print(a,b,c,d,e,f)
print(type(a)) # 查看变量类型
print(isinstance(b,bool)) # 判断变量类型

class A: pass
class B(A):pass
print("\n")
print(isinstance(A(),A))
print(type(A()) == A)
#print(isinstance(A(),B))
#print(type(A()) == B)
print(isinstance(B(),A))
print(type(B()) == A)
"""
type() 不会认为子类是一种父类类型。
isinstance() 会认为子类是一种父类类型。
"""
del A,B
print(isinstance(A(),A)) # 报错：未定义
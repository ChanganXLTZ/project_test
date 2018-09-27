# -*- coding:UTF-8 -*-
#!/usr/bin/env python3
"""
基本功能是进行成员关系测试和删除重复元素。
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，
因为 { } 是用来创建一个空字典。
"""
print('\n\b=====Python集合=====')
# 两种集合定义方法：
set_1 = {1,2,3,4,2,1,2,3,4,2,1,4}
set_2 = set([1,2,3,4,2,1,2,3,1])
print('第一种定义方法：',set_1)
print('第二种定义方法：',set_2)
del set_1,set_2

print('\n\b集合数据类型将自动去除重复元素')
list_s = ["Rick","And","Morty","And","Morty","Jerry","Beth"]
print('原始数组：',list_s)
student = set(list_s)
print('原始数组转化成集合：',student) # 将自动去除重复元素
print('重复元素被剔除\n')

# 成员测试
if "F" in student:
    print("F在这个集合中")
else:
    print("F不在这个集合中")
print( )

# 另一种定义方式，默认将引号内字符分开
set_c = set("abc")
print('字符串会被拆分：',set_c)
set_c = set(['abc'])
print('除非使用['']',set_c)
print( )

# 空字典只能用set()定义
print('空集合只能用set()定义,{}将会定义空字典')
set_empty = set()
print(type(set_empty))
set_empty = {}
print(type(set_empty),'\n')

# 集合可以运算
set_a = {"xy",1,"2"}
set_b = {"xy",2}
print("交集：",set_a & set_b) # 交
print("并集：",set_a | set_b) # 并
print("差集（a-b）：",set_a - set_b) # 差
print("差集（b-a）：",set_b - set_a)
print("对称集：",set_a ^ set_b) # 同时不存在的元素
set_d = set_a^set_b
set_e = (set_a-set_b)|(set_b-set_a)
if set_e == set_d:
    print(" ^ 是对称差")
else:
    print(" ^ 不是对称差")
# -*- coding:UTF-8 -*-
#!/usr/bin/env python3
print('\n\b=====Python字典=====')
dict_0 = {} # 大括号直接创建字典
# 字典第一种定义方法：
dict["grandpa"] = "Rick"
dict["boy"] = "Morty"
dict[0] = "0"
print('输出第一个字典：')
print(dict) # 输出整个字典
print('输出字典1的单个元素:',dict["boy"]) # 输出单个元素
print('输出字典1的单个元素:',dict[0])
# 字典第二种定义方法：
dict_1 = {"name" :"Jerry","job":"no","position":"father"}
print('字典的 .keys()方法返回值类型：',type(dict_1.keys()))
print('字典的 .values()方法返回值类型：',type(dict.values()))
dict_1_keys = list(dict_1.keys()) # 读取字典2关键字并转换成字符串
print('输出字典2的key：',dict_1_keys)
dict_values = list(dict.values()) # 读取字典1的值并转换成字符串
print('输出字典1的个值：',dict_values)

"""
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }。
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
"""
# 以下两种为命令框创建语法
# dict_2 = dict([("ID","00001"),("name","JerrySmith"),("position","commander")])
# dict_2 = dict(ID="00001",name="JerrySmith",position="commander")



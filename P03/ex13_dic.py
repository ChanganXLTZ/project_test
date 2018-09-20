# -*- coding:UTF-8 -*-
#!/usr/bin/env python3
dict = {} # 大括号直接创建字典
dict["grandpa"] = "Rick"
dict["boy"] = "Morty"
dict[0] = "0"
dict_1 = {"name" :"Jerry","job":"no","position":"father"}
print(dict) # 输出整个字典
print(dict["boy"]) # 输出单个元素
print(dict[0])

print(dict_1.keys())
print(dict.values())
print(type(dict_1.keys()))
print(type(dict.values()))
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



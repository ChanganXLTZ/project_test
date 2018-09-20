# -*- coding:UTF-8 -*-
#! /usr/bin/python3
dict1 = {'name':'Rick','age':70,'position':'science'}
print('name:',dict1['name']) # 索引
dict1['grandson'] = 'Morty' # 添加信息
dict1['position'] = 'scientist' # 修改信息
print(dict1)
del dict1['age']
print(dict1)
# del dict1
# print(dict1)
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
dict2 = {'A' : 1,'B' : 2,'A':3}
print(dict2)
# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行
# dict2 = {['A']:2,'b':1}
print(len(dict1)) # 计算键总数
print(str(dict1)) # 输出字典，以可打印的字符串表示。
print(type(str(dict1)))
print(dict2.clear()) # 清空字典
dict3 = dict1.copy()
print(dict3)
# dict3.fromkeys(['A','B','C'],[1,2,3])
# print(dict3)
print(dict3.get('name')) # 得到索引的值
if 'Rick' in dict1:
    print('属于该字典')

print(dict1.items()) # 遍历所有键 值
print('键类型',type(dict1.items()))
print(dict1.keys()) # 遍历所有键，可作为迭代器
print(dict1.values())
print()
dict1.setdefault('daughter') # 查找该键的值，不存在则存入None
print(dict1.items())
dict3.update(dict1) # 更新，把字典dict2的键/值对更新到dict里
print(dict3.items())
dict3.pop('position') # 删除某一对
print(dict3)
dict3.popitem() # 随机返回并删除字典中的一对键和值(一般删除末尾对)。
print(dict3)
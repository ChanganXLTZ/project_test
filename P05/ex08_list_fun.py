# -*- coding:UTF-8 -*-
#! /usr/bin/python3
list_1 = ["Rick","Morty",70,14]
print('元素二',list_1[1])
list_1[1] = 'Jerry'
print('更新后：',list_1)
del list_1[3]
print('删除后：',list_1)
list_2 = [9,2,3,4,5,1]
for x in list_2:
    print(x,end=' ') # 迭代
print()
list_3 = list_1+list_2 # 连接
print(list_3)
list_3 = [list_2,list_1] # 嵌套
print(list_3[1][1])
list_1.append('Beth')
list_1.append(30) # 队尾增加元素
print(list_1)
print(list_1.count(70)) # 计算元素出现次数
list_1.extend([10,20,'A']) # 队尾增加序列
print(list_1)
print(list_1.index('Beth')) # 求元素出现的最小索引
list_1.insert(3,'14') # 插入元素,索引为3 ,第4个元素
print(list_1)
print(list_1.pop(1)) # 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list_1.remove('A') # 移除列表中某个值的第一个匹配项
print(list_1)
list_1.reverse() # 反向列表中元素
print(list_1)
# print(list_1.sort(None,None,False)) # 对原列表进行排序 ???
list_3 = list_1.copy() # 复制
print(list_3,end=' ')
print(list_1)
list_3.clear() # 清空
print(list_3)
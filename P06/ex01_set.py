# -*- coding:UTF-8 -*-
#! /usr/bin/python3
set_empty1 = {} # 创建空字典不能用空大括号，建出来是字典
set_empty2 = set() #　正确的创建空集合的方法
print(type(set_empty1),type(set_empty2))

set_basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(set_basket) # 去重

alf1 = set('abcxyz')
alf2 = set('zucoys')
print(alf1-alf2) # 差
print(alf2-alf1)
print(alf1&alf2) # 交
print(alf1|alf2) # 并
print(alf1^alf2) # 对称差
a = {x for x in 'abracadabra' if x not in 'abc'} # ？

print('原始集合：',a)
a.add('as') # 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。
print('add增加数据：',a)
a.update('we','can') # 添加元素，且参数可以是列表，元组，字典等
print('update字符串：',a)
a.update({'we','can'}) # 注意区别
print('update集合，注意区别：',a)
a.update([1,4],[5,6])
print('update数组：',a)

a.remove('we') # 将元素 x 添加到集合 s 中移除，如果元素不存在，则会发生错误。
print(a)
a.discard('as') # 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。
print(a)
a.pop() # 我们也可以设置随机删除集合中的一个元素
print(a)
print(a.__len__()) # 长度 len()相同
if 5 in a:
    a.remove(5)
    print(a)



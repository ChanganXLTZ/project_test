# -*- coding:UTF-8 -*-
#!/usr/bin/env python3
list_a = [1,2,3,4,1,31,3,13,1,3]
list_b = ["a",23]
print(list_a)
print(list_a[1:2]) # 截取列表的返回值也是个列表
print(list_a[4],"\n")
print(list_b[:1]) # 与元组不同，不会有逗号
print(list_b[0:])
print(list_a[0:4] * 2) # 重复列表
print(list_a + list_b) # 连接列表
list_a[0:2] = ["a","w",3] # 列表元素可以修改
print(list_a)
list_str = ["asdfg","iweru","ewhg","jfig"]
list_str[0] = "q" # 此处的修改为覆盖
print(list_str)
list_str[:1] = [] # 注意区别
print(list_str)
list_str[0] = [] # 注意区别
print(list_str)
str1 = "ads"
print(str1)
str1 = "errt" # 字符串不能修改但可覆盖
print(str1)
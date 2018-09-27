# -*- coding:UTF-8 -*-
#!/usr/bin/env python3
list_a = [1,2,3,4,1,31,3,13,1,3]
list_b = ["a",23]
print('列表a：',list_a)
print('     截取元素[1:2]：',list_a[1:2]) # 截取列表的返回值也是个列表
print('     索引单个元素，索引为4：',list_a[4])
print('列表b：截取区间 [:1]:',list_b[:1]) # 与元组不同，不会有逗号
print('     截取区间 [0:]:',list_b[0:])
print('重复列表a[0:4]两次:',list_a[0:4] * 2) # 重复列表
print('连接列表a和列表b:',list_a + list_b) # 连接列表
list_a[0:2] = ["a","w",3] # 列表元素可以修改
print('修改之后的列表a：',list_a,'\n')

list_str = ["asdfg","iweru","ewhg","jfig"]
list_str[0] = "q" # 此处的修改为覆盖
print('字符串列表：',list_str)
list_str[:1] = [] # 注意区别
print('注意区别',list_str)
list_str[0] = [] # 注意区别
print('注意区别',list_str,'\n')

str1 = "ads"
print(str1)
str1 = "errt" # 字符串不能修改但可覆盖
print(str1)
print('字符串不能修改但可覆盖')
# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import keyword
print(keyword.kwlist)

"""
    多行注释
    。
"""
'''
    多行注释
    。
'''
item_one = 1
item_two = 2
item_thr = item_one \
    +item_two         #这是个换行符
print(item_thr,
      item_two)
item_four = [item_one,item_two,
             item_thr]  #{}[]中不需要换行符
print(item_four)
print(type(item_four))
pr_test1 = "转义\n字符"  '\n其中\是转义字符' # 字符串可以自动连接
pr_test2 = r"转义\n字符" # r 使转义字符 \ 不发生转义，这里的 r 指 raw，即 raw string。
print(pr_test1)
print(pr_test2)
pr_test3 = pr_test1 + pr_test2 # 也可以使用 + 连接字符串
print(pr_test3)
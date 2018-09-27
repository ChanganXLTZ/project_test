# -*- coding:UTF-8 -*-
#!/usr/bin/env python3

str_1 = "AbCdEfGhIjKlM"
print(str_1[1:-2]) # 从第2位到倒数第二位
print(str_1[2:]) # 从第3位到队尾
str_2 = str_1 * 2 # 重复输出
print(str_2)
str_3 = [[str_1],[str_2]]
print(str_1 , '测试1')
print(str_1 + '测试1')
print(str_3,['测试2']) # 逗号属于print函数的参数分隔符
print(str_3+['测试2']) # 加号相当于进行了连接操作
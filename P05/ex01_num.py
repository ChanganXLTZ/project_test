# -*- coding:UTF-8 -*-
#! /usr/bin/python3
val_1 = 10
val_2 = 20
val_3 = 30
del val_3
val_3 = 2.5e2 # 科学计数法
val_4 = 250
val_5 = 1e-10
val_6 = 0.0000000001
if val_3 == val_4:
    print("第一组相等")
else:
    print('第一组不相等')
if val_5 == val_6:
    print("第二组相等")
else:
    print('第二组不相等')

number_1 = 0xA0F # 十六进制
number_2=0o37 # 八进制
# 执行数值类型转化
print(number_1,number_2)
print(val_1)
val_1 = float(val_1)
print(val_1)
print(val_3)
val_3 = int(val_3)
print(val_3)
number_3 = complex(number_1,number_2)
print(number_3)

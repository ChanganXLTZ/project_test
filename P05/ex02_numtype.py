# -*- coding:UTF-8 -*-
#! /usr/bin/python3
print("注意除法结果无论整除与否均为浮点型")
print(type(10/2)) # 注意除法结果无论整除与否均为浮点型
print("整除与分子分母类型相关")
print(type(10//2)) # 整除与分子分母类型相关
print("分子分母有浮点型则结果位浮点型")
print(type(10.0//2)) # 分子分母有浮点型则结果位浮点型
print(type(10.0//2.0))
print(type(10//2.0))
print("混合计算产生浮点型")
print(type(3 * 3.75 / 1.5)) # 混合计算产生浮点型
print(round(100.0001,2)) # ??
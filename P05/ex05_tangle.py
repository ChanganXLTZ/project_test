# -*- coding:UTF-8 -*-
#! /usr/bin/python3
import math
x = 0.5
print(math.acos(x)) # 返回x的反余弦弧度值。
print(math.asin(x)) # 返回x的反正弦弧度值。
print(math.atan(x)) # 返回x的反正切弧度值。
print(math.atan2(1,1)) # 返回给定的 X 及 Y 坐标值的反正切值。
print(math.cos(80)) # 返回x的弧度的余弦值。
print(math.sin(80)) # 返回x的弧度的正弦值。
print(math.tan(80)) # 返回x的弧度的正切值。
print(math.hypot(1,2)) # 返回欧几里德范数 sqrt(x*x + y*y)。

Rad_a = math.pi/2
Deg_a = math.degrees(Rad_a)
print('弧度转换为角度',Deg_a) # 将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
print('将角度转换为弧度',math.radians(Deg_a)) # 将角度转换为弧度

print("圆周率",math.pi)
print("自然对数",math.e)
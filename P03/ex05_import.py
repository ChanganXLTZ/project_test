#!/usr/bin/env python3
import sys
for i in sys.argv:
    print(i)
print('sys.argv的数据类型为：',type(sys.argv))
path_s = sys.path
print("\n当前python3路径为",path_s)
print("路径为"+path_s[2]) # 此处包的属性为一字符串数组，前两个元素为空？
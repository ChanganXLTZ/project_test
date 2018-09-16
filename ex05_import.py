#!/usr/bin/env python3

import sys
for i in sys.argv:
    print(i)
path_s = sys.path
print("\npython3路径为" ,sys.path)
print(sys.path)
print("路径为"+ path_s[1]) # 这里调用函数的返回值为list型，无法整体直接输出屏幕
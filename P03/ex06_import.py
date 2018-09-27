#!/usr/bin/env python3
from sys import argv,path #注意逗号，引入指定成员
print("path:",path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
print('argv:',argv)
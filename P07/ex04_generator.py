#! /usr/bin/python3
import sys
def fibonacci(n):
    a,b,counter = 0,1,0
    while 1 :
        if (counter > n):
            return
        yield a # 使用了 yield 的函数被称为生成器（generator）。
        a,b = b,a+b
        counter += 1
# 在调用生成器运行的过程中，
# 每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

while 1:
    try:
        print(next(f),end=' ') # 调用一个生成器函数，返回的是一个迭代器对象。
    except StopIteration:
        sys.exit()

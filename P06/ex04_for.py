# -*- coding:UTF-8 -*-
#! /usr/bin/python3
print('''for循环使用格式：
for <variable> in <sequence>:
    <statements>
else:
    <statements>\n''')
# 以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体
for a in [1,2,3,4,5,5,6,7,7,8,8,9,9,10,12,13,14,56,78]:
    if a == 8:
        print('a = 8 了')
        break # 直接结束循环
    print('a：',a,end= ';')
print( )
# continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
for a in [1,2,3,4,5,5,6,7,7,8,8,9,9,10,12,13,14,56,78]:
    if a == 8:
        print('|a = 8| ',end=';')
        continue # 跳出本次循环
    print('a:',a,end= ';')
print( )

# 如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
for a in range(10):
    print(a,end=" ")
print( )
for a in range(5,10):
    print(a,end=' ')
print( )
for a in range(0,-15,-3):
    print(a,end=' ') # 第三个变量表示步长

print( )
list1 = list(range(10,1000,99)) # 可用于创建列表
print(list1)
# 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。
for a in range(6):
    print(a)
else:
    print('here is the end')
# 例如
for n in range(2, 20):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, '是质数')
while a in range(5):
    pass # Python pass是空语句，是为了保持程序结构的完整性，pass不做任何事情，一般用做占位语句.
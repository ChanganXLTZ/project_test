# -*- coding:UTF-8 -*-
#! /usr/bin/python3

matrax_a = [
    [1,2,3,4,5],
    [3,4,5,6,7],
    [5,6,7,8,9]
]
print(len(matrax_a[0]))
matrax_b = [[x[i] for x in matrax_a] for i in range(len(matrax_a[0]))]
matrax_c = [x[i] for x in matrax_a for i in range(len(matrax_a[0]))]
print('b',matrax_b)
print('c',matrax_c)
matrax_d = [[x[i] for x in matrax_b if x[i] >3] for i in range(len(matrax_b[0]))]
print('d',matrax_d)
del matrax_b[0][:]
print(matrax_b)
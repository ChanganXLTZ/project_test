# -*- coding:UTF-8 -*-
#! /usr/bin/python3

def Mprint(a,b):
    print(a)
    print(b)

Mprint('asd','qwe')
Mprint(b = '123',a = '567')

def print_name(name2 = 'Jerry',name1 = 'Beth'):
#    name1 = 'Beth'
    print('G:',name1)
    print('B:',name2)
    return
print_name('Jesica','Morty')
print_name('未赋值输出默认值')
print_name()
print_name(name1='Rick')
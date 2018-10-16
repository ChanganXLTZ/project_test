# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 10:46:26 2018

@author: LZC
"""

def Fibo(n):
    a,b = 0,1
    F = []
    i = 1
    while b<n:
        b,a = a+b,b
        F = F+[b]
        i += 1
    return F

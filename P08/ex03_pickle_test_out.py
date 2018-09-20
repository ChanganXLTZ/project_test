# -*- coding:UTF-8 -*-
#! /usr/bin/python3

import pickle

dat_1 = {
    'A' : '111',
    'B' : list(range(10)),
    'C' : []
}
list_self = list('abcxyz')
list_self = list_self * 2


with open('test.pkl','wb') as output_f:

    pickle.dump(dat_1,output_f)# Pickle dictionary using protocol 0.
    pickle.dump(list_self,output_f,-1)# Pickle the list using the highest protocol available.


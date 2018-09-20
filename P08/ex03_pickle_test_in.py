# -*- coding:UTF-8 -*-
#! /usr/bin/python3

import pickle
import pprint
with open('test.pkl','rb') as Input:
    data_1 = pickle.load(Input)
    data_2 = pickle.load(Input)
print(data_1)
pprint.pprint(data_2)
print(data_2)
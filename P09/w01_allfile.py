# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:00:50 2018
% 读取文件夹里文件
@author: ZhichaoLi
"""

#coding=utf-8
import os
import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

def GetFileList(dir, fileList):
　　newDir = dir
　　if os.path.isfile(dir):
　　　　fileList.append(dir.decode('gbk'))
　　elif os.path.isdir(dir): 
　　　　for s in os.listdir(dir):
　　　　#如果需要忽略某些文件夹，使用以下代码
　　　　#if s == "xxx":
　　　　#continue
　　　　newDir=os.path.join(dir,s)
　　　　GetFileList(newDir, fileList) 
　　return fileList


list = GetFileList('D:\\python\\work\\cp1\\game_name', [])      这个是获取目录文件

 

dirs = os.listdir('.\\')  获取目录下所有东西,包含文件和文件夹


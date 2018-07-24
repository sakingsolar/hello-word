# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 11:32:57 2018

@author: timi
"""

f=open('全国山西学校理科招生数.txt',encoding='utf-8').readlines()
ls=[]
data=[]
for line in f:
    ls.append(str(line.split('(')[1].split(',')[0]))
    data.append(int(line.split(',')[1].split(')')[0]))
print(ls)
print(data)
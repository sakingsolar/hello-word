# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 23:00:31 2018

@author: timi
"""

ls1=open('XML高考派城市.txt',encoding='gbk').readlines()
print('招生城市编号为：\n')
for n in range(1,32):  
    print(ls1[n].split('<li data-val=')[1].split('data-id')[0]+':'+ls1[n].split('claimCity')[1].split(')">')[0])

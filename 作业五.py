# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:51:27 2018

@author: timi
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ingore')
import json
data=json.loads(data)

def weather (a,b):
    print ('day'+str(a))
    print('天气情况:'+str(data['list'][b]['weather'][0]['main']))
    print('')
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)
weather(5,34)

def chart(a):
    data1=data['list'][a]['main']['temp']
    num=str('-')*int(data1)
    return num
print('这五天的温度折线图:')
print(' 1'+chart(2))
print(' 2'+chart(10))
print(' 3'+chart(18))
print(' 4'+chart(24))
print(' 5'+chart(36))

url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ingore')
import json
data=json.loads(data)

list=[]
def chart (a):
   return data['list'][a]['main']['temp']
a1=chart(2)
a2=chart(10)
a3=chart(18)
a4=chart(26)
a5=chart(34)
b=[a1,a2,a3,a4,a5]
print('这五天的天气温度从低到高排序：')
print(sorted(b))
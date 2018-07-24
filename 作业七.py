# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 20:11:56 2018

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
    print('温度:'+str(data['list'][b]['main']['temp']))
    print('气压:'+str(data['list'][b]['main']['pressure']))
    print('')
    a=str(data['list'][b]['weather'][0]['main'])
    if a=='Clear':
        print('天气很好，可以去远足！')
    elif a=='Rain':
        print('今日有雨，记得带伞！')
    elif a=='Clouds':
        print('今日多云，气温较低，注意保暖！')
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)
weather(5,34)

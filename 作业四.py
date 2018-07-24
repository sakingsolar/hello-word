# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:26:55 2018
=
@author: user
"""
city=input('please enter the name of the city you want to inquire')
import urllib.request as r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url.format(city)).read().decode('utf-8','ingore')
import json
data=json.loads(data)
main=data['list'][0]['weather'][0]['main']
print('the weather is the case:'+main)
print('第一天')
print(data['list'][2]['weather'][0]['main'])
print(data['list'][2]['main']['temp'])
print(data['list'][2]['main']['pressure'])
print(data['list'][2]['main']['temp_min'])
print(data['list'][2]['main']['temp_max'])
print('第二天')
print(data['list'][10]['weather'][0]['main'])
print(data['list'][10]['main']['temp'])
print(data['list'][10]['main']['pressure'])
print(data['list'][10]['main']['temp_min'])
print(data['list'][10]['main']['temp_max'])
print('第三天')
print(data['list'][18]['weather'][0]['main'])
print(data['list'][18]['main']['temp'])
print(data['list'][18]['main']['pressure'])
print(data['list'][18]['main']['temp_min'])
print(data['list'][18]['main']['temp_max'])
print('第四天')
print(data['list'][24]['weather'][0]['main'])
print(data['list'][24]['main']['temp'])
print(data['list'][24]['main']['pressure'])
print(data['list'][24]['main']['temp_min'])
print(data['list'][24]['main']['temp_max'])
print('第五天')
print(data['list'][34]['weather'][0]['main'])
print(data['list'][34]['main']['temp'])
print(data['list'][34]['main']['pressure'])
print(data['list'][34]['main']['temp_min'])
print(data['list'][34]['main']['temp_max'])

####打印温度折线图
print('第一天','-'*int(data['list'][2]['main']['temp']))
print('第二天','-'*int(data['list'][2]['main']['temp']))
print('第三天','-'*int(data['list'][2]['main']['temp']))
print('第四天','-'*int(data['list'][2]['main']['temp']))
print('第五天','-'*int(data['list'][2]['main']['temp']))
n=[data['list'][2]['main']['temp'],
      data['list'][10]['main']['temp'],
      data['list'][18]['main']['temp'],
      data['list'][26]['main']['temp'],
      data['list'][34]['main']['temp']]
print('排序后温度为')
print(sorted(n))

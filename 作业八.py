# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:15:48 2018

@author: timi
"""
import urllib.request as r
f=open('合肥淘宝数据.csv','w',encoding='gdk')
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E5%90%88%E8%82%A5&s={}&ajax=true'
for i in range (0,100):
    url1=url.format(i*44)
    try:
       data=r.urlopen(url1).read().decode('utf-8','ignore')
       f.write(str(data)+'\n')
       print('第{}行'.format(i+1))
    except Exception as err:
       print('此行有误')
f.close()

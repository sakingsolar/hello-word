# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 20:33:58 2018

@author: timi
"""
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json 
data=json.loads(data)
def look():
    for a in range (0,36):
        print('第'+str(a+1)+'商品的信息为：')
        print(data['mods']['itemlist']['data']['auction'][a]['title'])
        print(data['mods']['itemlist']['data']['auction'][a]['view_price'])
        print(data['mods']['itemlist']['data']['auction'][a]['item_loc'])
        print(data['mods']['itemlist']['data']['auction'][a]['view_sales'])
        if(a+1)%4==0:
            print('_'*40)
look()
 
ls=[]
def price():
    for a in range(0,36):
        c=float(data['mods']['itemlist']['data']['auctions'][a]['view_price'])
        ls.append(c)
    return ls
price()
x=sorted(ls)
print('商品价格从低到高：')
print(x)
b=ls(reversed(x))
print(b)

def free():
    for a in range (0,36):
        y=a
        if float(data['mods']['itemlist']['data']['auctions'][y]['view_fee'])==0.00:
            print('第{}件商品包邮'.format(y+1))
free()

# -*- coding: utf-8 -*-
"""
Created on Wed May 12 22:57:41 2021

@author: shahi
"""

num = 2.5
type(num)

num = 5
type(num)

num = 6+9j
type(num)

a = 5.6
b = int(a)
type(b)

b
5
k = float(b)
k
5.0
k = 6
c = complex(b,k)
c
(5+6j)
b<k
True
boll = b < k
bool

b > k
False
int(True)
1
int(False)
0

lst = [25,36,45,12]
type(lst)

s = {25,36,45,15,12,25}
s
{36, 12, 45, 15, 25}
type(s)

t = (25,36,4,57,12)
type(t)

str = "navin"
st = 'a'
type(st)

range(10)
range(0, 10)
list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(range(2,10,2))
[2, 4, 6, 8]
type(range(10))

d = {'navin':'samsung','rahul':'Iphone','kiran':'Oneplus'}
d
{'navin': 'samsung', 'rahul': 'Iphone', 'kiran': 'Oneplus'}
d.keys()
dict_keys = (['navin', 'rahul', 'kiran'])
d.values()
dict_values =(['samsung', 'Iphone', 'Oneplus'])
d['rahul']
'Iphone'
d.get('kiran')
'Oneplus'
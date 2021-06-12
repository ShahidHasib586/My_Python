# -*- coding: utf-8 -*-
"""
Created on Sat Jun 12 22:08:17 2021

@author: shahi
"""

My_list = [ i**2 for i in range (20) if  i%2==0]

#Set comprehention

list_item = ['Money', 'laptop', 'Ball', 'a', 'b', 'c']

set_item = {i for i in list_item if len(i)>1}

## if we use third braket then it will be a list: 
#set_item = [i for i in list_item if len(i)>1]
print(set_item)


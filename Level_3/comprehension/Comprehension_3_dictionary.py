# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 01:04:58 2021

@author: shahi
"""

#dictionary comprehension

list1 = ['name', 'country', 'occupation', 'university']

list2 = ['Shahid Ahamed', 'Bangladesh', 'Student', 'RUET']

my_dict = {i : j for i, j in zip(list1, list2)}

print(my_dict)
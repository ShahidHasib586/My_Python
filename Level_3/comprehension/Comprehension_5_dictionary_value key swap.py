# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 02:08:45 2021

@author: shahi
"""

#now we will see the use of comprehension

my_dict ={'carrer': 'talitaklk', 'country':'Bangladesh', 'name': 'Shahid', 'Age': '23'}

#now we will swap the key to value of dictionary

new_dic = {key: value for value, key in my_dict.items()}

print(new_dic)
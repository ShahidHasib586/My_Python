# -*- coding: utf-8 -*-
"""
Created on Tue May 25 18:51:48 2021

@author: shahi
"""

'''
Functional method in dictionary
'''
# copy() this function returans full copy of a dictionary

info_1 = {'name': 'Shahid A.Hasib', 'Nickname': 'Yami', 'ID': 1608014, 'Institution': 'RUET', 'Subject': 'Mechatronics Engineering', 'Graduation Year': '2022'}
info_2 = dict({'name': 'S.Tomal', 'Nickname': 'Tomal', 'ID': 1608025, 'Institution': 'RUET', 'Subject': 'Mechatronics Engineering', 'Graduation Year': '2022'})

info_1.copy()
# get function searches any key

info_1.get('name')

info_1.get('home', 'Dhaka')

# has_key(key): this function is use to check any specific key is present or not in the dictionary but it has been removed, we can do its='s work using in 

'name' in info_1
'MF' in info_2

#items() : this function returns dictionary as a list, inside the list every item stays as tuple in every tuple 0 index is key and 1 index is the value

info_1.items()

#keys() this function returns every key as a list

info_1.keys()

#values() this function returns every values as a list

info_2.values()
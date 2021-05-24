# -*- coding: utf-8 -*-
"""
Created on Sun May 24 19:22:58 2021

@author: shahi
"""

'''
Dictionary is kind of similar to list but there is also some differences, such as: dictionary is declared with {}. And there is no indexing like list in dictionary 
instead of indexing there is (key), string, integer, tuple can be used as key but ['key'] is unusable, As like list where index indicates a value the key does the same 
this value can be any data type (string, intiger, float, list, tuple, dictionary). Every item in dictionary is seperated by comma (,), every item has three 
part: in first part there is key, in middle part there is : (colon symbol), and in last there stays the value. every key in dictionary will be unique
but values can exists repeatedly.
'''
a = {}
type(a)

info_1 = {'name': 'Shahid A.Hasib', 'Nickname': 'Yami', 'ID': 1608014, 'Institution': 'RUET', 'Subject': 'Mechatronics Engineering', 'Graduation Year': '2022'}

'''
There is another way of declaring a dictionary we can use dict() function
'''

info_2 = dict({'name': 'S.Tomal', 'Nickname': 'Tomal', 'ID': 1608025, 'Institution': 'RUET', 'Subject': 'Mechatronics Engineering', 'Graduation Year': '2022'})

# we can access the item of a dictionary like we did in list, but the difference insted of the number we will need to indicate the key into the third braket []

info_1['name']
info_2['name']
info_1['ID']
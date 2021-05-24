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

# updating an item is easy in dictionary, we just need to assign new data in key

info_2['institution'] = 'KUET' # if there was a key in info_2 name institution then it will be updated otherwise a new element will be added

info_2['Phone no'] = 10078609

'''
If we need to add dictionary item to another dictionary then we will use the update function
'''

tomal = {'Hometown': 'Rajshahi', 'Favorite Game': 'Cricket'}

info_2.update(tomal)

'''
removing item in dictionary:  we can use del statement for removing an item
'''

del info_1['name']

# if we want to remove all elements of a dictionary we can use clear() function

info_1.clear()

# if we want to remove whole dictionary we can use del function

del info_1 # this will also erase the variable


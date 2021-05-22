# -*- coding: utf-8 -*-
"""
Created on Sat May 22 21:32:30 2021

@author: shahi
"""

'''
Adding item to tuple
'''
veg = ('onion', 'potato', 'ginger', 'cucumber')
cash = (8, 9 , 'money', 'note', (3, 4, 6), ['ball', 'bat', 'mouse'], 3.1416)

#we can't add item to tuple as list 

#veg[0] = 'carrot'

'''
however we can add new tuple and make the previous one a new tuple
'''
veg = veg+ ('carrot',)

# if we dont add the ',' comma in the last the python will consider it as string and will through TypeError: can only concatenate tuple (not "str") to tuple

'''
we can not remove any item from tuple
'''
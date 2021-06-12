# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 01:23:15 2021

@author: shahi
"""

'''
we used zip() function in dictionary comprehension to iterate 2 lists parallelly, this zip() function takes multiple iterable as parameter but reterns only 
one iterator (taple), where the n-number of taken taple parameter takes place in n-number of items.
'''
a = [i for i in range (11)]

b = [i for i in range (11, 21)]

c = zip(a,b)

list(c)

dic = {i:j for i, j in zip(a,b)}

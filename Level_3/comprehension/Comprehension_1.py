# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 22:03:40 2021

@author: shahi
"""

'''
Comprihention: the process of making iterator. Making iterator like list and dictionary from a sequence is called comprehension, we can also make stes
there are three part in a comprehention:
    
    1. Output expression: how every item will be in output iterator 
    2. Input Sequence: supplies the items that are required by output expression
    3. Conditional logic: this is optional, used for filtering item from input sequence
    
'''

#list comprehention is one line for loop that creates a list data structure

my_list = [i**2 for i in range (20) if i % 2 == 0]

print(my_list)




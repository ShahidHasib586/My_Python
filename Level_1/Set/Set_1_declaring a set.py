# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:22:58 2021

@author: shahi
"""

'''
Set: it's kind of a list but the main difference among them is in set every item can 
appear just for one time only, unlike list where items can be appear for multiple time,
every set operation (union, intersaction, difference) can be done in python. we use
{} this or set() function to create set in pthon
'''
A = {'orange', 'banana', 'pineapple', 'apple', 'mango'}

type(A)

#B = set('orange', 'banana', 'pineapple', 'apple', 'mango')
'''
this will through a TypeError: set expected at most 1 argument, got 5
'''
#type(B)

B = set('abracadabra')
print(B)

#set() function only takes one argument

C = {'orange', 'banana', 'pineapple', 'apple', 'mango', 'orange', 'banana','orange', 'banana', 'pineapple', 'apple', 'mango', 'pineapple', 'apple', 'mango'}

print(C)

# set will take one item one time 

'''
{} with this symbol , no empty set can be crted, for creating an empty set we need to use set() function
'''

'''
we can not access set item with the help of index number
A[0] will through a index error
'''
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 19:41:43 2021

@author: shahi
"""
'''
removing item from a list
'''
my_stuffs = ['phone', 'laptop', 'books', 'calculator', 'cricket bat', 'pant', 'keyboard']

my_school = [3.1416, 'money', [1,2,3,4,5, 'bag', 'bottle'], 'time' ]

'''
if we know the index number then we can use del() function, or if we don't know the index then we can use remove() function
'''

del my_stuffs[3]

my_school.remove('time')

#if we want to remove the lst item


del my_stuffs[-1]

'''
we can do this more easily with the help of pop() function

'''

my_school.pop()


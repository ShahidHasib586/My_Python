# -*- coding: utf-8 -*-
"""
Created on Sun May 23 19:22:58 2021

@author: shahi
"""

'''
Adding and removing item
'''
A = {'orange', 'banana', 'pineapple', 'apple', 'mango'}

type(A)

#we can add new item with the help of add() function

A.add('litchi')

'''
If we want to add multiple item at a time then add() function will no longer work, wee have to use update() function
'''
A.update('berry', 'grape')

# this will add every character individually

A.update({'berry', 'grape'}) #this will solve the problem

'''
we can use remove() function to remove an item from the set, butvif the item is absen in the set there will be a key error
'''
A.remove('apple')

# if we want to avoid the error we have to use discard function

A.discard('milk')

# pop() function removes the 1st tem of the set

A.pop()

# if we want to remove every item

A.clear()
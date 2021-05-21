# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:41:43 2021

@author: shahi
"""
'''
Updating the list item, we can update the list item with the help of a assignment operator
'''
my_stuffs = ['phone', 'laptop', 'books', 'calculator', 'cricket bat', 'pant', 'keyboard']

my_school = [3.1416, 'money', [1,2,3,4,5, 'bag', 'bottle'], 'time' ]

#if we want to replace books by phone and phone by books:

    
my_stuffs[0] = 'books'
my_stuffs[2] = 'phone'

#exchange time with money and list with pi with negative indexing

my_school[-4] = [1,2,3,4,5, 'bag', 'bottle']

my_school[-2] = 3.1416

my_school[-3] = 'time'

my_school[-1] = 'money'

##appened() function adds a new elemet at the end of the list

my_stuffs.append('mouse')
##my_stuffs.append('Python','Anaconda') 
'''
append takes exactly one arguments, this will through a type error

'''
'''
if we want to add a item anythere in the list we use insert function
'''
my_stuffs.insert(3,'Grameen Phone')

my_stuffs.insert(4,'01632552003')
##for other data types we need to use brackets to identify them as an object 
my_stuffs.insert(2,[1,2,3,4,5,6,7,8,9])
my_stuffs.insert(0,(123))

'''
if we want to add multiple item at a time we can use extend() function, it taks a list as argument but updates the list as individual item
'''
my_stuffs.extend([1,2,'baby'])

'''
We can do this more easily with the help of addition operator
'''
my_stuffs = my_stuffs + ['game', 'university', 'programming']

# adding multiple list in this list

my_stuffs = my_stuffs + [1, 2, 3] + [4, 5, 6] +[7 , 8, 9]


























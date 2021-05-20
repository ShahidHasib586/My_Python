# -*- coding: utf-8 -*-
"""
Created on Thu May 20 18:07:27 2021

@author: shahi
"""

my_stuffs = ['phone', 'laptop', 'books', 'calculator', 'cricket bat', 'pant', 'keyboard']

type(my_stuffs)

'''
a list can be with mixed datatype like int, fload, double, string, tople, set and even a list
'''

my_school = [3.1416, 'money', [1,2,3,4,5, 'bag', 'bottle'], 'time' ]

type(my_school)

'''
now we will try to access the items of the list, accesing the itams of the list is like strings, the index also starts from 0
'''
#positive indexing
my_stuffs[0]
my_stuffs[1]
my_stuffs[2]
my_stuffs[3]
my_stuffs[4]
my_stuffs[5]
my_stuffs[6]

#negative indexing

my_stuffs[-1]
my_stuffs[-2]
my_stuffs[-3]
my_stuffs[-4]
my_stuffs[-5]
my_stuffs[-6]
my_stuffs[-7]

'''
here we can see -7 and 0 index are same elements and -6 is 1 and so on
'''
#now we want to access the values from index 1 to 5

my_stuffs[1:6]

#here we can see 1 is included and 6 is excluded
#if we want to do the same thing with negative indexing

my_stuffs[-6:-1] 

#if we want to print the list accept its first 2 elements

my_stuffs[2:]

#if we want to print only the first two elements 

my_stuffs[:2]

#if we want to print the elements after a regular interval like one after one to the last one
#slicing the list
my_stuffs[0:7:2]

#checking the data type of the list

type(my_school[0])

type(my_school[1])

type(my_school[2])

type(my_school[3])

#accessing the list item inside a list
my_school[2][3]






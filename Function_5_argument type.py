# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:35:05 2021

@author: shahi
"""

#function parameter/ argument

'''there are 4 types of arguments i function'''

#Required Argument

def add(a, b, c):
    return a*b*c

temp = add(1,2,3)

print(temp)

#If we dont give the argument there will be a typeError


def add(a, b, c):
    return a*b*c

temp = add(1,2)#one argument is missing

print(temp)

#Keyword Argument
'''In the previous type of argument we just set the argument positionally, we can debine by its variable '''


def add(a, b, c):
    return a*b*c

temp = add(b=6,c=5,a=3)

print(temp)

#default argument 

'''In this we will give an argument a default value'''

def add(a, b, c=7):
    return a*b*c

temp = add(5,2)

print(temp)

##if we give the arameter value a new one we will find a new output
def add(a, b, c=7):
    return a*b*c

temp = add(5,2,9)

print(temp)

#Variable Length argument

'''in privious examples we used fixed arguments, but we dont how how meny inputs will be provided by the user'''

def add(*args):
    print(type(args))
    temp = 0
    for n in args:
        temp = temp+n
    return temp 
temp = add(1,2,3,4,5,6,7,8,9,10,11,12,13)

print(temp)

##if we give an star (*) before any function parameter, iyt can hold unlimited values, this creats a tuple and holds every value
##this called non-keyworded  variable length argument
'''
if we give two astaric symbol before parameter a keyworded variable will be created, this perameter creates a dictionary
'''
def add(**keyargu):
    print(type(keyargu))
    temp = 0#local variable
    for key in keyargu:
        temp = temp+keyargu[key]
    return temp 
temp = add(a=1,b=2,c=3,d=4)

print(temp)















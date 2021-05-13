# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:45:17 2021

@author: shahi
"""

#type casting or type conversion

'''
int()
float()
str()
tuple()
list()
set()
dict()

'''
a = input()
b = input()

print(type(a))

print(type(b))

#a*b wil show a type error

a = int(input())
b = int(input())

print(type(a))

print(type(b))

print(a*b)

#taking multiple input in one line using split function

a, b = input().split()

a = int(a)
b = int(b)

print(a*b)
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 23:29:10 2021

@author: shahi
"""

# problem: Finding a number in a list

my_list = [1, 3 , 5, 7, 11, 13, 15, 17, 20, 26, 31, 44, 54, 56, 65, 77, 94, 100]

print('Input the number:\n')

number = int(input())

first = 0

last = len(my_list)-1
found = False
cycle = 0

while first <= last and not found:
    midpoint = (first + last)//2
    if my_list[midpoint]==number:
        found = True
    else:
        if number < my_list[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1
            
    cycle += 1
        
print('found after', cycle, 'cycle')
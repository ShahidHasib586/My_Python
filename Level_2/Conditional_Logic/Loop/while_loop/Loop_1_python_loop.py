# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 21:17:15 2021

@author: shahi
"""

'''
Loop is a way of executing a conditional logic in a short period
'''
'''
suppose we want to print 1 to 10, we can do it by:
'''
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

'''
this rogram may seem fine but if we want to print 1 to 100 o 10000 then proceding this way will eat our time and it will not be convinent
to avoide this types of situation we can use loop for example:
'''

#we can use while loop to solve this poblem

n =1
while n<=10:
    print(n)
    
    n = n+1
    
#we can pront this with for loop

for n in range (1, 11):
    print(n)
    n=n+1
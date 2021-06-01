# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 21:17:15 2021

@author: shahi
"""

    
# for eveery n value print the n value increases to n+1 unless it reaches to 10

# when loop starts for first time the value of n is 1 than it is 2 .... when it is 11 the condition gets falues and loop stops

'''
Problem:2
calculate the series sumation: 1+2+3+4+......+100=?
'''

#solve_using for loop

sumation = 0

for n in range (1, 101):
    sumation = n+sumation
    n = n+1
   #print(sumation)#if we use for lopp here we can print every sumation from 1 to 100
print(sumation)



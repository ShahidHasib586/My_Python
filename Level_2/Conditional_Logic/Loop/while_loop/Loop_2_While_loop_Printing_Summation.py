# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 21:17:15 2021

@author: shahi
"""

'''
While loop
'''
'''
In while loop there are two part 1. logical expresion/condition and 2. Action
when a condition is true then the action will be executated and the action is executed untill the condition is true
while loop syntex is similar to if, a : symbol should be added after the condition
and indentation is necessary
'''
n = 1

while n<=10:
    print(n)
    n=n+1
    
# for eveery n value print the n value increases to n+1 unless it reaches to 10

# when loop starts for first time the value of n is 1 than it is 2 .... when it is 11 the condition gets falues and loop stops

'''
Problem:2
calculate the series sumation: 1+2+3+4+......+100=?
'''

#solve

n = 1
sumation = 0
while n<=100:
    sumation = n + sumation
    n = n+1
  # print(sumation) if we give print function inside the loop it will print every summation result from 1 to 100
print(sumation)

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 21:17:15 2021

@author: shahi
"""

    
# for eveery n value print the n value increases to n+1 unless it reaches to 10

# when loop starts for first time the value of n is 1 than it is 2 .... when it is 11 the condition gets falues and loop stops

'''
Problem:3
calculate the series sumation: 1+3+5+.....+97=?(without while loop)
'''
n = 1
summation = 0
while n<=97:
    summation = n+ summation
    n = n+2
    print(summation)


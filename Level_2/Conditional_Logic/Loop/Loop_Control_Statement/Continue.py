# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 20:03:33 2021

@author: shahi
"""

''' when loop finds continue statement it skips the next action but after that loop start to re-iterate and other are executed'''


for number in range (1, 11):
    
    if number == 5:
        continue
    print(number)
    
    #everything will be printed except the number 5
    

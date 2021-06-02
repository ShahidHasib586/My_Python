# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 20:12:48 2021

@author: shahi
"""

'''
pass: pass statement is a null operation, when it is executed nothing actually happens
'''
for number in range (1, 11):
    if number == 5:
        pass
    print(number)
    
#The pass statement is used as a placeholder for future code, when it is executed nothing happenes but you avoid getting an error when empty code is not allowed
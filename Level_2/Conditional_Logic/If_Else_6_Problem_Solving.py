# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 20:53:51 2021

@author: shahi
"""
'''
user will give a character input we need to determine whethere character is vaule or consonent 
'''
print("Please enter the character:\n")

character = input()

if character >= 'a' and character <= 'z' or character >= 'A' and character <= 'Z':
    if character in 'aeiouAEIOU':
        print ('You have entered a vowel')
        
    else:
        
        print('You have entered a consonent')
        
else:
    
    print('Invalid Input')
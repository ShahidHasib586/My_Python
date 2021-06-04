# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 19:39:58 2021

@author: shahi
"""

#problem3: Check an input is a pelendrom or not:
    
print('Please input your word:\n')

word = input()

word = word.casefold()

reversed_word = word[::-1]

if word == reversed_word:
    
    print('Great! It is a Pallindrome.')
    
else:
    
    print('It is not a Palindrome.')
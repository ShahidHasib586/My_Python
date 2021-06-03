# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 23:17:44 2021

@author: shahi
"""

#Loop Problem Solving

#Problem_1

'''
Show the multiplication table of a given number
'''
#soln(while_loop)
print('Enter the number which you want to see the multiplication table\n')

number =int(input())

count = 1
while count<=10:
    print(number, 'X', count, '=', number*count)
    count+=1
    
#___________________________________________________________________________

#soln(for_loop)

print('Enter the number which you want to see the multiplication table\n')

number =int(input())

for count in range (1, 11):
    print(number, 'X', count, '=', number*count)
    count+=1
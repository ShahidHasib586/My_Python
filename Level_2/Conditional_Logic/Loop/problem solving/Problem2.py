# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 06:31:42 2021

@author: shahi
"""

'''
print star rectangle from user input : *****
                                       *****
                                       *****
                                       *****
                                       ***** (if input=5)
'''

#__________________________________________________________________
#solve(while loop)
print('Enter the number:\n')

number = int(input())

temp = number

while number > 0:
    
    count = temp
   
    while count > 0:
       
        print('*', end ='')
        
        count -=1
        
    print()
    
    number -= 1


#__________________________________________________________________    
#solve(for loop)


print('Enter the number:\n')

number = int(input())

temp = number

for n in range (number):
    
    count = temp
    
    for i in range (count):
        
        print('*', end='')
        
        count-=1
    print()
    number-=1

#__________________________________________________________________    
    
#solve(without decrement for loop)   

print('Enter the number:\n')

number = int(input())

for i in range (number):
    for j in range (number):
        
        print('*', end='')
    print() 

#__________________________________________________________________

#solve(without nested loop)

print('Enter the number:\n')

number = int(input())

for i in range (number):
    print('*'*number)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        

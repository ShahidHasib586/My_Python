# -*- coding: utf-8 -*-
"""
Created on Mon May 17 21:07:50 2021

@author: shahi
"""
""" String Manupulation"""

'''
String can be in both single and double quote
'''
a = 'bangla'

b = 'desh'

print(a+b)

a = "bangla"

b = "desh"

print(a+b)

##If we use quotation inside a string it will show an error

#c = 'I love my 'Motherland', it is Bangladesh'

#so we use double quote insted of using single one 

c = "I love my 'Motherland', it is Bangladesh"

print (c)

#Use of back slash

'''
back slash avoids the next sing quote or double quote symbol
'''
c = 'I love my \'Motherland\', it is Bangladesh'
print(c)


# how to print backslash?

'''
If we give two backslash respectively one will be printed, again if we want to print new line 
we press \n and  if we want to print a tab  we write \t
'''
c = 'Bangladesh is my \'Motherland\'\\\'Homeland\'\n please support Palestine \t Israil is a terrorist state '
print(c)


#string value access

a = 'United'
b = 'state'
c = 'of America'

print(a)
print(b)
print(c)
#negative indexing
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
print(a[-6])
#positive indexing
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])

'''
here -6 and 0 have the same value, similarly: -5 is 1..... and -1 is 5
'''
#Accessing the values in a range of index
#prntig the values from 1 to 4 of the index
print(a[1:4])
#printing the value from 4 to last
print(a[4:])
#printing values with interval of 2
print(a[0:6:2])
'''
a[:2] by this we can access 1st two values of string and by a[2:] by this we can access the rest of the values of the string accept first 2
'''



































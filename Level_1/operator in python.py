# -*- coding: utf-8 -*-
"""
Created on Thu May 13 10:45:17 2021

@author: shahi
"""

# Arithmatic operator operator

'''
+ addition
- substraction
* multiplication
/ division
% modulis
** exponent
// flor divison operator (skips the number after decimal points)

'''
a = 5
b = 8

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a-b+5**7)
print(a//b)

# comparison operator

#comapres 

a = 9
b = 9
c = 7

d = 11

'''
== if both side operand are equal
!= if both side operand are not equal
> if right operand is grater than left operand
< if right operand is less than left operand
>= if right operand is grater or equal to left operand
<= if right operand is less or equal to left operand
'''
a == b

a != b

b > c

a < c

a <= b

c >= d

#Assignment operator

'''
Assigns the value

= assigns rith operand to left
+= adds both sides operand and place it to left operand 
-= Substracts left operand to right operand and place it to the left operand 
*= multiply both side operands
/= divide left operand to right oerand and place it to the left operand
'''
a = 5

print(a)

b = 3

print(b)

a += b

print(a)

a -= b

print(a)

a *= b

print(a)

a /= b

print(a)

#logical operator

'''
There are three logical operators in python 
and
or 
not
'''
a = 2
b = 2
c = 3
d = 3
a == b and c == b

a == c or c == d

not a == d

# membership operator 
'''
there are two membership operator in python
in: if left operand is found in right operand
not in:  if left operand is not found in right operand
'''
a = 'Dhaka'
b = 'ka'

a in b
b in a 

# identity operator 
'''
there are two identity operator in python
in: if both operand indicates the same object
not in:  if both operand do not indicates the same object
'''
a = 'Germany'
b = 12
c = 'money'
d = 'Germany'

a is b

c is d

a is d

###exercise

a = 8000
b = 8000

b is a






























'''
String formating
'''

a = 'English'

print(a)

print('My favorite language is:', a)

##If we want to print by variable formating

print('My favorite language is: %s' %a)

#here %s symbol is string formating symbol (for intiger %d, for float %f)

'''
How many number we want to print afer decimal point can be controlled by %f
'''

number = 3.1415926535897

print(number)

print('%.2f' %number)
print('%2f' %number)
print('%.6f' %number)

b = 'Bangla'

print('My favorite languages are:', a, 'and', b)

print('My favorite languages are: %s and %s' %(a,b))
















































'''
In python we will find three conditional logic except loop: if, elif(else if), else. At the end of every conditional statement we have to use ':' symbol
'''
# if condition
a = 5

'''if a<10:
print('True')
this will through a indentation error, 
'''
if a> 4:
    print('Every thing is good')

# if else condition

a = int(input())

if a == 10:
    print('You Have Entered the correct number')
    
else:
    print('wrong')
    
# if, elif, else

b = int(input())

if b > 0:
    print('%s is a positive number' %b)
    
elif b == 0:
    print('%s is nither positive nor negative' %b)
    
else:
    print('%s is a negative number' %b)
    
# nested if-else

a = int(input())

if a < 10:
    if (a%2==0):
        print('%s is less, Yes' %a)
    else:
        print('%s is less, No' %a)
else:
    if (a%3==0):
        print('%s is Greater, Yes' %a)
    else:
        print('%s is Greater, No' %a)


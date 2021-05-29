'''
Non-Zero/ Null value
In pyton every non-zero and non-null value is true, onthe other hand zero r null value is False

'''

a = 5

if a:
    print(True)
    
else:
    print(False)

a = 0

if a:
    print(True)
    
else:
    print(False)
    
a = not None

if a:
    print(True)
    
else:
    print(False)

a = None

if a:
    print(True)
    
else:
    print(False)

## we can think that is and == operator operation is same but these are not same, isoperator checks whethere two variable is pointing same object or not 
# whereas == operator checks: whether two varibales are poining the same  object or its value is equal or not

a = [1, 2, 3]

b = a
b is a

b == a

b = a[:]

b is a

b == a

## another example

4 is 2**2

4 == 2**2

1000 is 10**3

1000 == 10**3

# in python every intiger is cash until 256, for this incase of small intiger indise 256 range is operator is showing result accordingly. 

# if__name == "__main__"
# if__name == "__main__":
    #we will use this condition












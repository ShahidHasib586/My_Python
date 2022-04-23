#loop control statements
#change loop execution from its normal sequence 
#break = use to terminate the loop entirely 
#continue = skips the next itertion of the loop
#pass = does nothing , acts as a place holder

# break
'''

while True:
    name = input ("Enter Your name: ")
    if name !="":
        break 
   
     '''
#phone_number = '01768-575-420'
for i in range(1,21):
    if i == 13:
        continue
    print(i)
'''
for i in range (1,21):
    
    if i == 13:
        pass
    else:
        print(i)
'''
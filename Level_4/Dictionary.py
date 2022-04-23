'''
Dictionary = A changable, unordered collection of unique key: value pairs
'''
capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'Russia': 'Moscow'}
'''
print(capitals['Russia'])

print(capitals.get('Germany'))

print(capitals.keys())

print(capitals.values())


print(capitals.items())

for key,value in capitals.items():
    print()
'''   
    #dictionary mutable
capitals.pop('India')    
capitals.clear()
capitals.update({"Germany":"Berlin"})
for key,value in capitals.items():
    print(key, value)
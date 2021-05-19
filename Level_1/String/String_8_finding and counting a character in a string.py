#counting a string and finding

"""
len() finction returns the length of a string
"""

a = 'Supperposition'
len(a)
"""
count function counts the character appering several time
"""

a.count('p')
'''here we counted the number of thimes that c appears in the sentence , secoundly we counted 
the number of time c appears in the sentence after index 5 and tirdly we counted the number of time c appears between 
index 5 to 9
'''
sen = 'How can a clam cream in a clean cream can'
sen.count('c')
sen.count('c', 5)
sen.count('c', 5, 9)
'''
how we can find in which indexes the character appears?
'''
sen.find('c')

# this returns the 1st index value where c apperas

sen.find('c', 5)

# this returns the apperance of first c after index 5

'''
we can use index() function to do the same job as find() but if index 
function don't find the character it returns a valueError where find function
returns -1 value
'''
sen.find('z')
##sen.index('z')
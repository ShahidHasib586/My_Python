#replacing and spliting the string
sen = 'How can a clam cream in a clean cream can?'
#replace finction replaces a character in the string with the given character
sen.replace('c', 'd')

'''
If we want to remove the last ? (question mark)
'''
sen.replace('?', '')

# this çan be done with the help of strip function, the character that is given to this function's parameter if the character is appered in first or last to the string the strip function removes the character

sen.strip('?')

# now if we want to split the string by white space and make a list


sen.split(' ')

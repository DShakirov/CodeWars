import re

def kebabize(string):
    newstr = ''
    for letter in string:
        if letter.isalpha():
            if letter.isupper():
                newstr += '-' + letter.lower()
            else:
                newstr += letter
    return newstr.strip('-')
    

string = 'CAMEL'
print(kebabize(string))
word = "camelCasing"
def breakCamelCases(x):
    newstr = ''
    for letter in x:
        if letter.isupper():
            newstr += ' '
        newstr += letter
    return newstr
word = breakCamelCases(word)
print (word)

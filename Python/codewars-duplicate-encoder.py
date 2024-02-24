string = "PhxMp()( !@gOc(!"
newstring = ''
for letter in string.casefold():
    print(letter)
    if string.casefold().count(letter) >1:
        newstring += ')'
    else:
        newstring += '('
print (newstring)
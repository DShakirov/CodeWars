string = '. .'
counter = 0
lst = []
for letter in string.lstrip():
    if letter in '.-':
        if counter ==2:
            for letters in lst:
                lst.pop()
        lst.append(letter)
        counter = 0
    if letter == ' ':
        lst.append(letter)
        counter +=1
        if counter == 3:
            continue
print (''.join(lst))

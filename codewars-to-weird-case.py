def to_weird_case(string):
    lst = string.split(' ')
    newword = ''
    for words in lst:
        counter = 0
        newword += ' '
        for letter in words:
            
            if counter%2 == 0:
                newword += letter.upper()
            else:
                newword += letter.lower()
            counter +=1
    
    return newword.strip()
    



print(to_weird_case('Weird string case'))


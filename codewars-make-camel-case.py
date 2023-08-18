string = 'test case'

def camel_case(string):
    lst = string.split(' ')
    
    newword = ''
    for word in lst:
        counter = 0
        for letter in word:
            if counter == 0:
                newword += letter.capitalize()
            else:
                newword += letter
            counter +=1
    print (newword)
        
camel_case(string)
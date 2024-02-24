import re
from collections import Counter
def valid_parenthesis(string):

    for i in range(len(string)):
        print (string[:i])
        print('Закрывающих:',string[:i].count(')'), ' Открывающих:', string[:i].count('(') )
        if string[i] == '(':
            print('Закрывающая!')
            if int(string[:i].count(')')) > int( string[:i].count('(')):
            
                return False
    return True
    #string = re.sub('[^()]', '', string)
    #return (string.startswith('(') and string.endswith(')')) and (string.count('(') == string.count(')'))


print(valid_parenthesis('())(()'))
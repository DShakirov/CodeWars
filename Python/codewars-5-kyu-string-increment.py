import re

def increment_string(string):
    if not string:
        return '1'
    if string[-1].isalpha():
        return string + '1'
    ciphers = re.search(r'[0-9]*$', string).group(0)
    string = re.split(r'[0-9]*$', string)
    if re.match(r'[1-9]',ciphers):
        print('Строка начинается не с нуля')
        ans = str(int(ciphers) + 1)
        ans = string[0] + ans
    else:
        ans = str(int(ciphers) + 1)
        if len(ans) < len(ciphers):
            ans = string[0] + '0'*(len(ciphers)-len(ans)) + ans
        else:
            ans = string[0] + ans
    #elif re.match(r'(0)[1-9]', ciphers):
        #print('Строка начинается с 1 нуля')
        #ans =  str(int(ciphers) + 1)
        #if len(ans) == len(ciphers):
            #return string[0] + ans
        #else:
            #return string[0] + '0' + ans

    #else:
        #print("Строка начинается более чем с одного нуля")
    
    return ans

print(increment_string('foo0099'))
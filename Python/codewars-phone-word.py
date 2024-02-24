
def phone_word(num):
    phone_dict = {
        '2':'a', '22':'b', '222':'c',
        '3': 'd','33': 'e', '333': 'f',
        '4': 'g', '44': 'h', '444': 'i',
        '5': 'j', '55': 'k', '555':'l',
        '6': 'm', '66': 'n', '666':'o',
        '7': 'p', '77': 'q', '777': 'r', '7777': 's',
        '8': 't', '88': 'u', '888': 'v',
        '9': 'w', '99': 'x', '999': 'y', '9999': 'z',
        '0': ' '
         }
    ans = ''
    number = num[0]
    newword = ''
    for numbers in num:
        if numbers == number:
            newword += numbers
        else:
            newword += ' '+ numbers
            number = numbers
    print (newword)
    newword = newword.split(' ')
    print (newword)
    for ciphers in newword:
        for key, val in phone_dict.items():
            if ciphers == key:
                ans += val
            else:
    print (ans)
    
    
num = '443355555566604466690277733099966688'
phone_word(num)
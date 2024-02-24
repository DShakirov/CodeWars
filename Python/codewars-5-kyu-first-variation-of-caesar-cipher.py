import math

def moving_shift(s, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    part = ''
    res =[]
    lenght = math.ceil(len(s)/5)
    for counter,letter in enumerate(s):       
        if letter.lower() in alphabet:
            ind = (alphabet.index(letter.lower()) + counter + shift)%26
            if letter.isupper():
                part += alphabet[ind].upper()
            else:
                part += alphabet[ind]
        else:
            part += letter
        if (counter+1)%lenght ==0:
            res.append(part)
            part = ''
    if part != '':
        res.append(part)
    if len(res) ==4:
        res.append('')
    return res

def demoving_shift(s, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ans  = ''
    for counter, letter in enumerate(''.join(s)):
        if letter.lower() in alphabet:
            ind = (alphabet.index(letter.lower()) - counter - shift)%26
            if letter.isupper():
                ans += alphabet[ind].upper()
            else:
                ans += alphabet[ind]
        else:
            ans += letter
    return ans

print(moving_shift('I should have known that you would have a perfect answer for me!!!',1))
print(demoving_shift(['J vltasl rlhr ', 'zdfog odxr ypw', ' atasl rlhr p ', 'gwkzzyq zntyhv', ' lvz wp!!!'], 1))
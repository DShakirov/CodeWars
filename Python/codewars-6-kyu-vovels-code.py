def encode(st):
    vovels = 'aeiou'
    res = ''
    for letter in st:
        if letter not in vovels:
            res += letter
        else:
            res += str(vovels.index(letter) +1)
    return res

def decode(st):
    vovels = 'aeiou'
    res = ''
    for letter in st:
        if letter.isalpha():
            res += letter
        else:
            res += vovels[int(letter) -1]
    return res

print(encode('hello'))
print(decode('h2ll4'))
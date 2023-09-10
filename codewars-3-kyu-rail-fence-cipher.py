from math import ceil

def encode_rail_fence_cipher(string, n):
    res = ['' for i in range(n)] #рельсы, пока пустые
    direction = 'down'
    counter = 0
    for letter in string:
        res[counter] += letter
        print(letter, counter, direction)
        if direction == 'down':
            if counter == n - 1:
                direction = 'up'
            else:
                counter += 1   
        if direction == 'up':
            if counter == 0:
                direction = 'down'
                counter += 1
            else:
                counter -=1
    return ''.join(res)

def decode_rail_fence_cipher(string, n):
    #cycle = int(len(string)/((n*2) - 2))
    #определяем длину элементов на рельсах для расшифровки
    res, rails = '', [0 for i in range(n)] #рельсы, пока пустые
    direction = 'down'
    counter = 0
    for letter in string:
        rails[counter] += 1
        if direction == 'down':
            if counter == n - 1:
                direction = 'up'
            else:
                counter += 1   
        if direction == 'up':
            if counter == 0:
                direction = 'down'
                counter += 1
            else:
                counter -=1
    for k, j in enumerate(rails):
        rails[k] = string[:j]
        string = string[j:]

#cобираем шифра воедино
    direction = 'down'
    counter = 0
    length = sum([len(x) for x in rails])
    for i in range(length):
        res += rails[counter][0]
        try:
            rails[counter] = rails[counter][1:]
        except:
            continue
        if direction == 'down':
            if counter == n - 1:
                direction = 'up'
            else:
                counter += 1   
        if direction == 'up':
            if counter == 0:
                direction = 'down'
                counter += 1
            else:
                counter -=1
    return res




#print(encode_rail_fence_cipher('Hello, world!', 3))
print(decode_rail_fence_cipher('IA_EZS_ELYLK_UZERLIPL', 3))

"""
['H    o  o      !',
 ' e l, W r  d', 
 '  l      l']
"""
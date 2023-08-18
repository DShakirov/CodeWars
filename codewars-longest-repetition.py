def longest_repetition(chars):
    symbol = ''
    counter = 0
    lst = []
    for letter in chars:
        if letter == symbol:
            counter +=1
        else:
            lst.append((symbol, counter))
            symbol = letter
            counter = 1
    lst.append((symbol, counter))
    print (lst)
    ans = max(lst, key = lambda x: x[0])
    return ans
chars = 'bbbaaabaaaa'
print (longest_repetition(chars))
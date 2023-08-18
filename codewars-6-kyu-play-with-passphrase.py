def play_pass(s, n):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans = ''
    for counter, symbol in enumerate(s):
        if symbol.isalpha():
            ind = (alphabet.index(symbol)+n)%len(alphabet)
            if counter%2 == 0:
                ans += alphabet[ind]
            else:
                ans += alphabet[ind].lower()
        elif symbol.isnumeric():
            ans += str(9 - int(symbol))
        else:
            ans += symbol
    return ans[::-1]

print(play_pass("BORN IN 2015!", 1))
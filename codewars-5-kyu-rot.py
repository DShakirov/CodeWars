def rot13(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ans = ''
    for letter in message:
        if letter.lower() in alphabet:
                x = alphabet.index(letter.lower()) + 13 if (alphabet.index(letter.lower()) + 13) < 26 else alphabet.index(letter.lower()) - 13
                if letter.islower():
                    ans += alphabet[x]
                else:
                    ans += alphabet[x].upper()
        else:
            ans += letter
    return ans

print(rot13("EBG13 rknzcyr."))
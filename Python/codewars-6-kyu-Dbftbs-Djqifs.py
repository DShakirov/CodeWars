def encryptor(key, message):
    ans = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in message:
        if letter.isalpha():
            if letter.islower():
                ans += alphabet[(alphabet.index(letter)+ key)%26]
            else:
                ans += alphabet[(alphabet.index(letter.lower())+ key)%26].upper()
        else:
            ans += letter    
    return ans

print(encryptor(13, 'Caesar Cipher'))
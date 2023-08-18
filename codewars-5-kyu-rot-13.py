def rot13(string):
    ans = ''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in string:
        if letter in letters and letter.islower():
            if letters.index(letter) + 13 < len(letters):
                ans += letters[letters.index(letter) + 13]
            else:
                ans += letters[13 + letters.index(letter) - len(letters)]
            print(letter, letters.index(letter))
        elif letter.lower() in letters:
            if letters.index(letter.lower()) + 13 < len(letters):
                ans += letters[letters.index(letter.lower()) + 13].upper()
            else:
                ans += letters[13 + letters.index(letter.lower()) - len(letters)].upper()
        else:
            ans += letter               
    return ans
print (rot13('do i return to original ?!'))
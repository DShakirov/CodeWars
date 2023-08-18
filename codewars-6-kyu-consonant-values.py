def consonant_value(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    counter = 0
    ans = []
    for letter in string:
        if letter in consonants:
            counter += alphabet.index(letter) + 1
        else:
            ans.append(counter)
            counter = 0
    if counter >0:
        ans.append(counter)   
    return max(ans)


print(consonant_value('cozy'))
def vovel_one(string):
    vovels = ['a', 'e', 'i', 'o', 'u']
    newstr = ''
    for letter in string:
        if letter in vovels:
            newstr += '1'
        else:
            newstr += '0'
    return newstr

string = 'aeiou, abc'
print(vovel_one(string))
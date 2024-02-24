words = "the-stealth-warrior"
lst = list(words)
print (lst)
counter = 0
for letter in lst:
    if letter in '-_':
        
        lst.remove(letter)
        lst[counter]=lst[counter].upper()
    counter+=1
print (lst)
xwords = ''.join(lst)
print(xwords)
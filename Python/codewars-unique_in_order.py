unique_in_order = ('AAAABBBCCDAABBB')
counter = str
newlist = []
for letter in list(unique_in_order):
    if letter == counter:
        continue
    else:
        newlist.append(letter)
        counter = letter
print (newlist)
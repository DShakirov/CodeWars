from collections import Counter
cards = ['A4Y', 'A4R']
A = 11
B = 11
newdict = dict(Counter(cards))
print (newdict)
for key, val in newdict.items():
    if val  > 1:
        if key.startswith('B'):
            B -=1
        else:
            A -=1
    elif 'R' in key:
        if 'B' in key:
            B -=1
        else:
            A -=1
print(A,B)
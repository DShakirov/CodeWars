from collections import Counter

string = input('Enter a string: ')
x = dict(Counter(string.casefold()))
print(x)
counter = 0
for key, val in x.items():
    if val >1:
        counter += 1
        print (key, val, counter)

print('Answer is', counter)

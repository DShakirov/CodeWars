from collections import Counter
string = input ('Enter a string: ')
if len(string) == 0:
    ans = None
x = Counter(string.casefold())
print(x)

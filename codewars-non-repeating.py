from collections import Counter
string = input ('Enter a string: ')
if len(string) == 0:
    ans = None
x = dict(Counter(string))
print(x)
for key, val in x.items():
    print (key,val)

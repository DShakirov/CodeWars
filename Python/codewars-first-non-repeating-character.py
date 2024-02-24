from collections import Counter
string = input ('Enter a string: ')
if len(string) == 0:
    ans = None
x = dict(Counter(string.casefold()))
print(x)
for key, val in x.items():
    if key == ' ':
        continue
    elif val == 1:   
        print ('Answer is: ',key)
        for letters in string:
            if key in letters.casefold():
                ans = letters
                break
        break
    ans = None
print(ans)
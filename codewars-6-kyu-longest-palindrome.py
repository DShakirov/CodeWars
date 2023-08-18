import re
from itertools import product
def longest_palindrome(string):
    length = len(string)
    ans = []
    for a,b in product(range(length+1), range(length+1)):
        if (a > b) :
            newstr = string[b:a]
            if len(newstr) == length:
                break
            elif len(newstr) == 1:
                newstr_reversed = newstr
            else:
                newstr_reversed = newstr[::-1]
            
            if newstr+newstr_reversed in string:
                ans.append(len(newstr+newstr_reversed))
            elif newstr+newstr_reversed[1:] in string:
                ans.append(len(newstr+newstr_reversed[1:]))
            print (newstr,newstr_reversed, a, b, ans)
    return max(ans)
string = "baabcd"
print(longest_palindrome(string))
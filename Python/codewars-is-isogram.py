from collections import Counter

def is_isogram(string):
    counter = Counter(string.casefold())
    for key, val in counter.items():
        if val >1:
            return False
    return True

string = 'Oregon'
is_isogram(string)

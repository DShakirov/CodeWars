from collections import Counter

def find_unique(arr):
    counter = Counter(arr)
    for key, val in counter.items():
        if val == 1:
            return key


print(find_unique([ 1, 1, 1, 2, 1, 1 ]))
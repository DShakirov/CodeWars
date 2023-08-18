from itertools import combinations
def get_all_subsequences(string):
    subsequences = []
    for i in range(len(string)+1):
        x = list(combinations(string, i))
        for t in x:
            if ''.join(t):
                subsequences.append(''.join(t))
    return sorted(subsequences, key = len, reverse=True)

def get_longest_common_subsequence(string1, string2):
    k = get_all_subsequences(string2)
    j = get_all_subsequences(string1)
    for item in k:
        if item in j:
            return item
print(get_longest_common_subsequence( "132535365" , "123456789"))
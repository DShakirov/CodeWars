arr =  ['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']
def find_unique_string(arr):
    newarr = []
    for words in arr:
        newarr.append(sorted(words.casefold()))
       
    newarr.sort()
    return newarr
print (find_unique_string(arr))
    
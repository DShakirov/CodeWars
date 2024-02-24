from collections import Counter
def unicalize(string):
    return ''.join(list(set(sorted(string.lower())))) 

def find_uniq(lst):
    res = [unicalize(i) for i in lst if unicalize(i)]
    cnt = Counter(res)
    print(cnt)
    res = cnt.most_common()[-1][0]
    for i in lst:
        if unicalize(i) == res:
            return i


print(find_uniq(['    ', '  ', ' ', 'a', ' ', '']))
#print(f'fuck{unicalize("   ")}fuck')
#print(f'fuck{unicalize("  ")}fuck')
#print(unicalize('victor'))
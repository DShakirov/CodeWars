from itertools import product
def smallest(n):
    res = []
    y = str(n)
    for i,k in product(range(len(y)), range(len(y))):
        j = list(y)
        elem = j[i]
        j.pop(i)
        j.insert(k, elem)
        res.append([int(''.join(j)), i, k])
    return min(res)

print(smallest(209917))

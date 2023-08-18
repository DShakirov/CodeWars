def josephus(items,k):
    i = 0
    res = []
    x = len(items)
    while len(res) < x:
        j = (i + k -1)%len(items)
        print(i, len(items))
        res.append(items[j])
        del items[j]
        i = j if j < len(items) else 0
    return res


print(josephus([1,2,3,4,5,6,7],3))
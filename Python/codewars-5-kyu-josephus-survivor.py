def josephus_survivor(n, k):
    ans = []
    i = 0
    items = [i for i in range(1, n +1)]
    while len(items) > 0:
        j = (i + k - 1)%len(items)
        ans.append(items[j])
        del items[j]
        i = j if j < len(items) else 0
    return ans[-1]
print(josephus_survivor(7,3))